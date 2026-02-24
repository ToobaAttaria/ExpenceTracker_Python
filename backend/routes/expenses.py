from fastapi import APIRouter, HTTPException
from database import supabase
from schemas import Expense

router = APIRouter()

# Get all expenses
@router.get("/expenses")
def get_expenses():
    response = supabase.table("expenses").select("*").execute()
    return response.data


# Add new expense
@router.post("/expenses")
def add_expense(expense: Expense):
    data = {
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date
    }

    response = supabase.table("expenses").insert(data).execute()
    return response.data


# Update existing expense
@router.put("/expenses/{id}")
def update_expense(id: str, expense: Expense):
    data = {
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date
    }

    response = supabase.table("expenses").update(data).eq("id", id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Expense not found")
    return response.data


# Delete expense
@router.delete("/expenses/{id}")
def delete_expense(id: str):
    response = supabase.table("expenses").delete().eq("id", id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Deleted"}