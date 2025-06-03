import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def edit_expense(self):
        if not self.expenses:
            print("수정할 지출이 없습니다.\n"); return
        self.list_expenses()
        try:
            idx = int(input("수정할 번호를 입력하세요: ")) - 1
            if 0 <= idx < len(self.expenses):
                e = self.expenses[idx]
                print(f"현재: {e}")
                new_cat = input(f"새 카테고리 [{e.category}]: ") or e.category
                new_desc = input(f"새 설명 [{e.description}]: ") or e.description
                amt_input = input(f"새 금액 [{e.amount}]: ")
                try:
                    new_amt = int(amt_input) if amt_input != "" else e.amount
                except ValueError:
                    print("금액이 잘못 입력되었습니다.\n"); return

                # 값 갱신
                e.category = new_cat
                e.description = new_desc
                e.amount = new_amt
                print("지출이 수정되었습니다.\n")
            else:
                print("잘못된 번호입니다.\n")
        except ValueError:
            print("유효한 숫자를 입력하세요.\n")
