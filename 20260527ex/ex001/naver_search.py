import tkinter as tk
import random

# 게임 설정 값
GRID_SIZE = 20      # 한 칸의 크기 (픽셀)
GRID_COUNT = 20     # 게임 판의 가로/세로 칸 수
GAME_SPEED = 100    # 게임 속도 (밀리초 단위, 낮을수록 빠름)

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 눈치 챙긴 제미나이의 스네이크 게임 🔥")
        
        # 캔버스 생성
        self.canvas = tk.Canvas(
            root, 
            width=GRID_SIZE * GRID_COUNT, 
            height=GRID_SIZE * GRID_COUNT, 
            bg="black"
        )
        self.canvas.pack()
        
        # 점수 표시 레이블
        self.score_label = tk.Label(root, text="점수: 0", font=("Arial", 14))
        self.score_label.pack()
        
        # 방향키 입력 바인딩 (WASD 없음, 오직 방향키만!)
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        
        self.reset_game()

    def reset_game(self):
        """게임 초기화"""
        self.score = 0
        self.score_label.config(text=f"점수: {self.score}")
        
        # 뱀 초기 위치 (가운데 3칸, 머리는 맨 오른쪽)
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = "Right"
        
        self.food = None
        self.create_food()
        self.is_game_over = False
        
        # 게임 루프 시작
        self.game_loop()

    def create_food(self):
        """뱀과 겹치지 않는 무작위 위치에 음식 생성"""
        while True:
            x = random.randint(0, GRID_COUNT - 1)
            y = random.randint(0, GRID_COUNT - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, new_dir):
        """반대 방향으로의 역주행을 막으면서 방향 변경"""
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir

    def move_snake(self):
        """뱀을 한 칸 이동시키고 충돌 및 음식 섭취 체크"""
        head_x, head_y = self.snake[0]
        
        # 현재 방향에 따른 새로운 머리 좌표 계산
        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)
            
        # 벽에 부딪히거나 자기 몸에 부딪히면 게임 오버
        if (new_head[0] < 0 or new_head[0] >= GRID_COUNT or
            new_head[1] < 0 or new_head[1] >= GRID_COUNT or
            new_head in self.snake):
            self.is_game_over = True
            return
            
        # 머리 추가
        self.snake.insert(0, new_head)
        
        # 음식을 먹었는지 확인
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"점수: {self.score}")
            self.create_food()
        else:
            # 음식을 안 먹었으면 꼬리를 잘라서 전진 효과를 냄
            self.snake.pop()

    def draw(self):
        """화면 새로 그리기"""
        self.canvas.delete("all")
        
        # 음식 그리기 (빨간색 동그라미)
        fx, fy = self.food
        self.canvas.create_oval(
            fx * GRID_SIZE, fy * GRID_SIZE,
            (fx + 1) * GRID_SIZE, (fy + 1) * GRID_SIZE,
            fill="red", outline="white"
        )
        
        # 뱀 그리기 (머리는 초록색, 몸통은 연두색)
        for i, (sx, sy) in enumerate(self.snake):
            color = "#00FF00" if i == 0 else "#80FF80"
            self.canvas.create_rectangle(
                sx * GRID_SIZE, sy * GRID_SIZE,
                (sx + 1) * GRID_SIZE, (sy + 1) * GRID_SIZE,
                fill=color, outline="black"
            )

    def game_loop(self):
        """지정된 속도마다 반복 실행되는 게임 메인 루프"""
        if not self.is_game_over:
            self.move_snake()
            self.draw()
            self.root.after(GAME_SPEED, self.game_loop)
        else:
            # 게임오버 메시지 출력
            self.canvas.create_text(
                (GRID_SIZE * GRID_COUNT) // 2,
                (GRID_SIZE * GRID_COUNT) // 2,
                text="GAME OVER\n스페이스바를 눌러 재시작",
                fill="white", font=("Arial", 16, "bold"), justify="center"
            )
            self.root.bind("<space>", lambda event: self.restart())

    def restart(self):
        """게임 재시작"""
        self.root.unbind("<space>")
        self.reset_game()

# 프로그램 실행
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()