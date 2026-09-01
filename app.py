from flask import Flask, request

app = Flask(__name__)

expenses = []
next_expense_id = 1

@app.route("/")
def home():
    return {"message":"Expense Tracker API"}

@app.route("/expenses", methods=["POST"])
def create_expense():
    global next_expense_id

    data = request.get_json()

    expense = {
        "id": next_expense_id,
        "amount": data["amount"],
        "category": data["category"],
        "description": data["description"],
        "date": data["date"]
    }

    expenses.append(expense)

    next_expense_id += 1

    return expense, 201

if __name__ == "__main__":
    app.run(debug=True)
