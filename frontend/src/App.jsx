import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"
import FraudDetectionForm from "./components/FraudDetectionForm"
import TransactionForm from "./components/TransactionForm"
import TransactionList from "./pages/TransactionList"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />}></Route>
        <Route path="/predict" element={<FraudDetectionForm/>}></Route>
        <Route path="/transaction" element={<TransactionForm/>}></Route>
        <Route path="/transactions" element={<TransactionList/>}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App