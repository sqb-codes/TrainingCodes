Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.clear()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.clear()
t.circle(100)
t.left(45)
t.circle(100)
t.left(45)
t.circle(100)
t.left(45)
t.circle(100)
t.clear()
t.reset()
for i in range(1,21):
    t.circle(5 * i)
    t.left(45)

    
t.clear()
t.reset()
t.speed(0)
for i in range(1,51):
    t.circle(5 * i)
    t.left(45)

    
t.clear()
t.reset()
colors = ["red", "blue", "green", "orange", "purple"]
for i in range(36):
    t.color(colors[i])
    t.forward(150)
    t.right(170)

    
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    t.color(colors[i])
IndexError: list index out of range
t.reset()
t.clear()
for i in range(36):
    t.color(colors[i % len(colors)])
    t.forward(150)
    t.right(170)

    
t.reset()
t.clear()
>>> t.speed(0)
>>> for i in range(72):
...     t.color(colors[i % len(colors)])
...     t.forward(350)
...     t.right(170)
... 
...     
>>> t.clear()
>>> for i in range(100):
...     t.color(colors[i % len(colors)])
...     t.circle(5 * i)
...     t.left(45)
... 
...     
>>> t.clear()
>>> t.width(2)
>>> t.width(5)
>>> t.width(2)
>>> for i in range(36):
...     t.circle(100)
...     t.right(10)
... 
...     
>>> t.clear()
>>> for i in range(72):
...     t.color(colors[i % len(colors)])
...     t.circle(100)
...     t.right(10)
... 
...     
>>> t.clear()
>>> for i in range(72):
...     t.color(colors[i % len(colors)])
...     t.circle(100)
...     t.right(10)
... 
...     
