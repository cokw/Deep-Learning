## 데이터
shoes = 270.0
height = 170.0

## 파라미터 
w = 0.1
b = 0.2

## 학습률
learning_rate = 0.00001

print("학습 전 : ",w*270+b)

## 순전파
def forward(x):
    return w*x+b

## 학습(순전파 + 역전파)
def opt():
    global w, b
    loss = (170 - forward(270)) **2
    w -= -2 * 270 * (170 - forward(270)) * learning_rate
    b -= -2 * (170 - forward(270)) * learning_rate

## 100번 반복
for i in range(100):
    opt()
    print(w, b)

print("학습 후 : ",w*270+b)
