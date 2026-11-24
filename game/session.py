from .pot import Pot

BASIC_RAMEN_PRICE = 3000

class GameSession:
    # 초기화
    def __init__(self):
        self.pot = Pot()
        self.order_pending = True
        self.sales = 0

    # 주문 확인
    def serve(self, now):
        # 대기 주문 X
        if not self.order_pending:
            return False
        
        # 대기 주문 O, 상태가 "ready"가 아닐 경우
        if self.pot.state(now) != "ready":
            return False

        # 대기 주문 O, 상태 "ready"인 경우
        self.order_pending = False
        self.sales += BASIC_RAMEN_PRICE
        self.pot = Pot()    # 냄비 초기화
        return True