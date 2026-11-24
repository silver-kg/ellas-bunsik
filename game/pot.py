COOK_SECONDS = 7    # 라면 완성 판정 시각
BURN_SECONS = 12    # 라면 타는 판정 시각

class Pot:
    # 초기화
    def __init__(self) -> None:
        self.has_water = False
        # noodle 넣고 시간 측정 시작됨
        self.noodle_added_at: float | None = None
        self.has_soup = False

    # 물 넣기
    def add_water(self) -> bool:
        if self.has_water:
            return False

        self.has_water = True
        return True

    # 면 넣기
    def add_noodles(self, now: float) -> bool:
        # 물 넣은 후 & 면 넣기 전에만 가능!
        if not self.has_water or self.noodle_added_at is not None:
            return False

        self.noodle_added_at = now
        return True

    # 스프 넣기
    def add_soup(self, now:float) -> bool:
        # 면 넣은 후 & 스프 넣기 전에만 가능!
        if self.noodle_added_at is None or self.has_soup:
            return False
        # 면 넣고 나서 COOK_SECONDS가 지나면 완성됨 -> 스프 넣을 수 없음
        if now - self.noodle_added_at >= COOK_SECONDS:
            return False

        self.has_soup = True
        return True

    # Pot 상태
    def state(self, now: float) -> str:
        # noodle 없을 때
        if self.noodle_added_at is None:
            return "water_only" if self.has_water else "empty"
        
        elapsed = now - self.noodle_added_at

        # BURN_SECONS 초과 시
        if elapsed >= BURN_SECONS:
            return "burnt"
        # 초과는 X, 스프는 X일 경우
        if not self.has_soup:
            return "needs_soup" if elapsed < COOK_SECONDS else "incomplete"
        # 초과는 X, 스프는 O, COOK_SECONS 초과 시
        if elapsed >= COOK_SECONDS:
            return "ready"
        return "cooking"