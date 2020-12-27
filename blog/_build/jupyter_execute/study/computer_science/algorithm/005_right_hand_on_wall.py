#!/usr/bin/env python
# coding: utf-8

# # 우선법 알고리즘

# ### 1. 알고리즘 개요
# 우선법(혹은 좌선법)은 미로찾기 알고리즘 중 하나이다. 어떤 미로를 빠져나갈 때 오른쪽(혹은 왼쪽)벽을 계속 따라가다보면 언젠가는 출구에 다다를 수 있다는 알고리즘이다. 이 때 오른쪽(혹은 왼쪽)은 절대적인 방향이 아니라 탐색자의 기준에서 바라본 방향을 의미한다.

# ### 2. 수도코드 (우선법 기준)
# 
# ```c
# while("아직 미로안에 있다면"){
#         
#     "오른쪽으로 한번 회전"
#             
#     while("탐색자 앞에 벽이 있다면"){
#             
#         "벽이 없을때까지 왼쪽으로 회전"
#     }
#         
#     "앞으로 한칸 전진"
# }
# ```

# ### 3. 실제로 어떻게 움직일까?
# 
# ![](https://user-images.githubusercontent.com/38183241/103154305-f511ec80-47d9-11eb-95d3-f935c3746458.png)

# ### 4. 알고리즘 구현
# 수도코드와 이미지만 봐서는 잘 이해가지 않을 수 있다. 직접 소스코드를 구동시켜서 움직임을 확인해보자.

# In[ ]:


from IPython.display import clear_output
import time
import copy


# In[ ]:


class Mouse:
    
    def __init__(self, x, y, d):
        """
        생쥐 클래스 (마이크로 마우스)
        
        :param x: 생쥐의 x좌표
        :param y: 생쥐의 y좌표
        :param d: 생쥐의 방향표시
        """
        
        self.x = x
        self.y = y
        self.d = d
        
    def turn_left(self):
        """
        왼쪽으로 회전
        """
        
        if(self.d == '▲'): self.d = '◀'
        elif(self.d == '▼'): self.d = '▶'
        elif (self.d == '◀'): self.d = '▼'
        elif (self.d == '▶'): self.d = '▲'
    
    def turn_right(self):
        """
        오른쪽으로 회전
        """
        
        if(self.d == '▲'): self.d = '▶'
        elif(self.d == '▼'): self.d = '◀'
        elif (self.d == '◀'): self.d = '▲'
        elif (self.d == '▶'): self.d = '▼'
    
    def go_ahead(self):
        """
        보고있는 방향에서 앞으로 한 칸 전진
        """
        
        if(self.d == '▲'): self.y -= 1
        elif(self.d == '▼'): self.y += 1
        elif (self.d == '◀'): self.x -= 1
        elif (self.d == '▶'): self.x += 1
    
    def see_ahead(self):
        """
        생쥐의 바로 앞칸 x,y좌표를 반환
        """
        
        if(self.d == '▲'): return self.x, self.y - 1
        elif(self.d == '▼'): return self.x, self.y + 1
        elif (self.d == '◀'): return self.x - 1, self.y 
        elif (self.d == '▶'): return self.x + 1, self.y


# In[ ]:


class Maze:
    
    def __init__(self, speed):
        """
        미로 클래스의 생성자. 
        
        :param speed: 화면갱신 속도
        """
        self.speed = speed
        self.grid =          [['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■'],
          ['□', '□', '■', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '■', '□', '□', '□', '■'],
          ['■', '□', '■', '□', '■', '■', '■', '□', '■', '■', '■', '■', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '□', '■', '□', '□', '□', '■', '□', '□', '□', '□', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '□', '■', '■', '■', '□', '■', '■', '■', '■', '■', '■', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '□', '□', '□', '■', '□', '□', '□', '□', '□', '■', '□', '□', '□', '■', '□', '■'],
          ['■', '□', '■', '■', '■', '□', '■', '□', '■', '■', '■', '□', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '□', '□', '□', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '■', '■', '■', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '□', '□', '□', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '■', '■', '■', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '□', '□', '□', '□', '□', '□', '■', '□', '□', '□', '■', '□', '■', '■', '■', '□', '■'],
          ['■', '□', '■', '■', '■', '■', '■', '□', '■', '□', '■', '■', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '□', '□', '□', '□', '□', '■', '□', '□', '□', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '□', '■', '■', '■', '■', '■', '■', '■', '■', '■', '□', '■', '□', '■', '□', '■'],
          ['■', '□', '■', '□', '■', '□', '□', '□', '□', '□', '□', '□', '□', '□', '■', '□', '□', '□', '■'],
          ['■', '□', '■', '□', '■', '□', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '□', '□', '■'],
          ['■', '□', '■', '□', '□', '□', '■', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '■'],
          ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']];


    def print_maze(self, mouse):
        """
        grid에 생쥐의 현재 위치를 표시하고 1/스피드 초마다 화면갱신
        time과 ipython.display의 clear_output함수 활용
        """
        
        current = copy.deepcopy(self.grid)
        current[mouse.y][mouse.x] = mouse.d
        clear_output(wait=True)
        
        for row in current:
            for elem in row:
                print(elem, end=' ')
            print('\n', end='')
        
        time.sleep(1 / self.speed)


# In[ ]:


class MazeApp:
    

    
    def __init__(self, mouse, maze):
        """
        우선법 알고리즘을 구현하는 클래스
        
        :param mouse: 위치와 방향이 초기화된 생쥐 클래스
        :param maze: 속도와 그리드가 초기화된 미로클래스
        """
        
        self.mouse = mouse
        self.maze = maze
        self.dest_x = 0
        self.dest_y = 1

        
    def still_in_maze(self):
        """
        생쥐가 아직 미로를 빠져나가지 못했는지를 표시하는 함수
        도착지점인 (dest_x, dest_y)에 도달했는지 여부를 나타냄
        """
        
        finish = (self.mouse.y == self.dest_y and                   self.mouse.x == self.dest_x)
        
        return not finish
    
    
    def wall_ahead(self):
        """
        생쥐의 시선방향에서 한칸 앞에 벽이 있는지 여부를 나타냄
        """
        
        x, y = self.mouse.see_ahead()
        return self.maze.grid[y][x] == '■'
    
    
    def turn_left(self):
        """
        생쥐를 왼쪽으로 회전시키고 화면을 갱신함
        """
        
        self.mouse.turn_left()
        self.maze.print_maze(self.mouse)
    
    
    def turn_right(self):
        """
        생쥐를 오른쪽으로 회전시키고 화면을 갱신함
        """
        
        self.mouse.turn_right()
        self.maze.print_maze(self.mouse)
        
        
    def go_ahead(self):
        """
        생쥐를 한칸 앞으로 전진시키고 화면을 갱신함
        """
        
        self.mouse.go_ahead()
        self.maze.print_maze(self.mouse)
    
    
    def finish_animation(self):
        """
        생쥐가 도착지점에 도착했을 때 애니메이션
        """
        
        self.maze.speed = 5
        length = len(self.maze.grid)
        
        for i in range(length):
            for j in range(length):
                self.maze.grid[i][j] = '■'
            self.maze.print_maze(Mouse(0,0,'■')) 
        
 
    def right_hand_on_wall(self, finish_animation=True):
        """
        우선법 알고리즘.
        수도코드와 최대한 비슷하게 구현하였음
        """
        
        while self.still_in_maze():
            self.turn_right()
            
            while self.wall_ahead():
                self.turn_left()
            
            self.go_ahead()
        
        # 마지막 위치에 도착하면 애니메이션    
        if finish_animation == True:
            self.finish_animation()
           


# In[ ]:


# 알고리즘 실행부
mouse = Mouse(17, 17, '▲')
maze = Maze(speed=5)
maze_app = MazeApp(mouse, maze)
maze_app.right_hand_on_wall()


# ### 5. 최단경로 탐색
# 
# > https://youtu.be/IngelKjmecg
# 
# 이렇게 누가 미로를 더 빨리하는지 탈출하는지 경쟁하는 대회가 있다. 이런 대회 혹은 태스크를 Micromouse라고 한다. (위 영상 참고) 영상을 보면 초반에 가능한 경로들을 모두 탐색하고나서 두번째 탐색부터는 필요없는 경로는 가지않고 최단경로로 이동한다. 탐색했던 경로중 중복된 경로를 제거하여 최단경로를 만들 수 있다. 

# In[ ]:


def override(super_class):
    def overrider(method):
        assert(method.__name__ in dir(super_class))
        return method
    return overrider


class MicromouseApp(MazeApp):
    """
    위에서 구현한 MazepApp을 상속해서 구현.
    """
    
    def __init__(self, mouse, maze):
        """
        생쥐의 위치를 초기화시키기 위해
        생성자에서 초기 위치값을 미리 저장해놓음
        """
        self.paths = []
        self.init_x = mouse.x
        self.init_y = mouse.y
        super(MicromouseApp, self).__init__(mouse, maze)
        
    
    @override(MazeApp)
    def go_ahead(self, store=True):
        """
        MazeApp의 go_ahead()를 오버라이딩
        경로 리스트에 이동경로를 추가하는 부분을 추가함
        """
        self.paths.append((self.mouse.x, self.mouse.y))
        super(MicromouseApp, self).go_ahead()
    
    
    def find_duplicate_paths(self):
        """
        중복경로를 찾아주는 함수
        
        루프에서 현재 i번째 경로라면 j = i + 1번째 부터 끝까지 싹 가봤는데 
        만약 출발지인 i번째 경로로 다시 돌아온적이 있다는 것은 막다른 골목을 
        만나서 빠져나온 것이라고 볼 수 있음. (그외엔 같은 곳으로 갈 이유 X)
        
        때문에 i에서 시작해서 다시 i로 돌아오기 까지 그 사이 경로들은
        굳이 갈 필요가 없는 경로라는 것을 의미하고, 이 경로들을 전부 세서 리턴함.
        """
        
        path_size = len(self.paths)
        dup_path_idx = []
        
        for i, path in enumerate(self.paths):
            j = i+1
            while(j < path_size):
                if self.paths[j] == path:
                    for k in range(i, j):
                        dup_path_idx.append(k)
                j += 1
            
        return list(set(dup_path_idx))

    
    def make_shortest_paths(self, dup_path_idx):
        """
        찾아낸 중복경로를 기존 경로에서 제거하여
        최적의 경로를 만들어줌.
        """
        
        shortest_paths = []
        for i, path in enumerate(self.paths):
            if i not in dup_path_idx:
                shortest_paths.append(path)
        
        return shortest_paths
    
    
    @override(MazeApp)
    def right_hand_on_wall(self, finish_animation=True):
        """
        가장 먼저 우선법 알고리즘을 사용해 미로를 파악한 뒤,
        최단경로를 찾아내서 최단경로 탐색을 시도함.
        """
        
        # 모든 경로를 탐색하여 최단경로 생성
        super(MicromouseApp, self).right_hand_on_wall(False)
        dup_path_idx = self.find_duplicate_paths()
        shortest_path = self.make_shortest_paths(dup_path_idx)
        
        # 다시 처음 위치로 돌려놓음
        self.mouse.x = self.init_x
        self.mouse.y = self.init_y
        self.mouse.d = '◆'
        
        # 최단경로 미로탐색
        for x, y in shortest_path:
            self.mouse.x = x
            self.mouse.y = y
            self.maze.print_maze(self.mouse)
        
        # 마지막 위치에 도착하면 애니메이션 
        if finish_animation:
            self.finish_animation()      


# In[ ]:


# 알고리즘 실행부
mouse = Mouse(17, 17, '▲')
maze = Maze(speed=500)
micromouse_app = MicromouseApp(mouse, maze)
micromouse_app.right_hand_on_wall()


# ### 6. 우선법의 한계
# 
# ![](https://user-images.githubusercontent.com/38183241/103154307-f511ec80-47d9-11eb-8658-0b1671679c78.png)
# 
# 우선법은 만능의 미로 탈출 알고리즘처럼 보이지만 실제로는 그렇지 않다. 만약 순환경로를 만나게 된다면 계속 한쪽 벽만 잡고 가기때문에 계속 뱅뱅 돌게 된다. 이런 문제를 해결하려면 BFS, DFS, 다익스트라, A-star등 더욱 고차원적인 경로탐색 알고리즘을 사용해야한다.

# In[ ]:


# 알고리즘 실행부
mouse = Mouse(4, 11, '◀')
maze = Maze(speed=5)
maze_app = MazeApp(mouse, maze)
maze_app.right_hand_on_wall()


# ### 7. Reference
# > https://youtu.be/3RitBJgbqsQ
# 
