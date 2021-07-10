from collections import deque
class SnakeGame:
​
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.score = 0
        self.foods = food
        self.w, self.h = width, height
        self.pos = (0, 0)
        self.body = set([(0,0)]) ### for O(1) body check
        self.body_deque = deque([(0,0)])
        self.dirr = {
            "U" : (-1, 0),
            "R" : (0, 1),
            "L" : (0, -1),
            "D" : (1, 0)
        }
        
    def move(self, direction: str) -> int:
        self.pos = [a+b for a, b in zip(self.pos, self.dirr[direction])]
        x, y = self.pos
        if(x < 0 or x >= self.h or y < 0 or y >= self.w):
            return -1
        if(self.score < len(self.foods) and self.pos == self.foods[self.score]):
            self.score += 1
        else:
            self.body.remove(tuple(self.body_deque.popleft()))
        if((x, y) in self.body):
            return -1
        self.body_deque.append(self.pos)
        self.body.add((x, y))
        return self.score
    
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        
        
​
​
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
