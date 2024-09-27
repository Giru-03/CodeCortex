from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note,Transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle
import pandas as pd # type: ignore
import hashlib
from datetime import datetime
import random
from django.contrib.auth.decorators import login_required


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class PredictFraudView(APIView):
    with open('random_forest_model.pkl', 'rb') as model_file:
        RFC = pickle.load(model_file)
    with open('category_encoder.pkl', 'rb') as enc_file:
        category_encoder = pickle.load(enc_file)
    with open('cc_num_encoder.pkl', 'rb') as cc_file:
        cc_num_encoder = pickle.load(cc_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    def post(self, request, *args, **kwargs):
        try:

            # Extract datetime and parse it
            datetime_str = request.data.get('datetime')

            datetime_obj = datetime.fromisoformat(datetime_str)

            # Prepare the input data
            transaction_details = {
                'amt': float(request.data.get('amt')),
                'zip': int(request.data.get('zip')),
                'category': request.data.get('category'),
                'cc_num': request.data.get('cc_num'),
                'trans_day': datetime_obj.day,
                'trans_hour': datetime_obj.hour,
                'trans_month': datetime_obj.month,
                'trans_year': datetime_obj.year,
                'trans_minute': datetime_obj.minute
            }
            
            input_data = pd.DataFrame([transaction_details])

            # Ensure columns are in the expected order
            input_data['category'] = self.category_encoder.transform(input_data['category'])
            input_data['cc_num'] = self.cc_num_encoder.transform(input_data['cc_num'])
            
            # Scale numerical features
            input_data[['amt', 'zip']] = self.scaler.transform(input_data[['amt', 'zip']])
            # Ensure that the input has the same features as the model
            # input_data = input_data[X.columns]
            # print(input_data)

            # prediction = self.RFC.predict(input_data)
            # print(prediction)
            random_value = random.randint(0, 1)
            prediction = bool(random_value)

            return Response({'is_fraud': prediction}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@login_required
@api_view(['POST'])
def create_transaction(request):
    user = request.user
    amount = request.data.get('amount')
    zip_code = request.data.get('zip_code')
    category = request.data.get('category')
    cc_num = request.data.get('cc_num')
    datetime_str = request.data.get('datetime')

    # Convert string to datetime object
    trans_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

    # Calculate blockchain hash (simple hash for example purposes)
    blockchain_hash = hashlib.sha256(f"{amount}{zip_code}{category}{cc_num}{datetime_str}".encode()).hexdigest()

    # Create transaction object
    transaction = Transaction.objects.create(
        user=user,
        amount=amount,
        zip_code=zip_code,
        category=category,
        cc_num=cc_num,
        trans_day=trans_datetime.day,
        trans_month=trans_datetime.month,
        trans_year=trans_datetime.year,
        trans_hour=trans_datetime.hour,
        trans_minute=trans_datetime.minute,
        blockchain_hash=blockchain_hash
    )

    return Response({'message': 'Transaction created successfully'}, status=status.HTTP_201_CREATED)


@login_required
@api_view(['GET', 'DELETE'])
def transactions(request, pk=None):
    user = request.user

    if request.method == 'GET':
        # Fetch transactions for the current user
        transactions = Transaction.objects.filter(user=user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # Delete the selected transaction by pk
        try:
            transaction = Transaction.objects.get(pk=pk, user=user)
            transaction.delete()
            return Response({'message': 'Transaction deleted successfully'}, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
