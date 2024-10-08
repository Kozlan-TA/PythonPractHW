## Задача 1. Стек
Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры данных на основе уже существующих. Одним из таких “базовых” структур является стек.  
Стек - это абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).  

Простой пример: стек из книг на столе. Единственной книгой, чья обложка видна, является самая верхняя. Чтобы получить доступ к, например, третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.  

Напишите класс, который реализует Стек и его возможности (достаточно будет добавления и удаления элемента).  

После этого напишите ещё один класс “Менеджер задач”. В менеджере задач можно выполнить команду “новая задача”, в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе Стэка (не наследование!).  При выводе менеджера в консоль все задачи должны быть отсортированы по приоритету: чем меньше число, тем выше задача.  

Вот пример основной программы:  
```python
manager = TaskManager()  
manager.new_task("сделать уборку", 4)  
manager.new_task("помыть посуду", 4)  
manager.new_task("отдохнуть", 1)  
manager.new_task("поесть", 2)  
manager.new_task("сдать дз", 2)  
print(manager)  
```

Результат:  
1 отдохнуть  
2 поесть; сдать дз  
4 сделать уборку; помыть посуду  
  
Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами  

## Задача 2. Кэширование запросов
Контекст
Вы разрабатываете программу для кэширования запросов к внешнему API. Часто повторяющиеся запросы занимают много времени, поэтому вы решаете создать класс LRU Cache (Least Recently Used Cache), который будет хранить ограниченное количество запросов и автоматически удалять самые старые при достижении лимита. Это позволит значительно ускорить повторяющиеся запросы, так как данные будут браться из кэша, а не отправляться повторно.  
Задача  
Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита, удаляет самые давние (самые старые) использованные элементы.  
Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.  
```python
@property
def cache(self): # этот метод должен возвращать самый старый элемент
    ...
@cache.setter
def cache(self, new_elem): # этот метод должен добавлять новый элемент
    ...
```

Советы  
Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные элементы, а не давно добавленные, так как давно добавленный элемент может быть популярен, и его удаление не поможет ускорить новые запросы.  
Пример:  

```python
# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)


# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")


# # Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3


# Получаем значение по ключу
print(cache.get("key2")) # value2


# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")


# Выводим обновлённый кэш
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
```

Ожидаемый вывод в консоли:  
  
LRU Cache:  
key1 : value1  
key2 : value2  
key3 : value3  
  
value2  
  
LRU Cache:  
key3 : value3  
key2 : value2  
key4 : value4  

## Задача 3. Кэширование для ускорения вычислений
Контекст
Вы разрабатываете программу для оптимизации вычислений чисел Фибоначчи. Числа Фибоначчи вычисляются рекурсивной функцией, каждое число равно сумме двух предыдущих чисел.  Однако вы заметили, что при больших значениях чисел Фибоначчи вычисления занимают значительное время, так как многие значения вычисляются повторно. Вам поручено создать декоратор, который кэширует результаты вызова функции и позволяет избежать повторных вычислений для одних и тех же аргументов.  

Задача:  
Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) результаты вызова функции и, при повторном вызове с теми же аргументами, возвращает сохранённый результат.  

Примените его к рекурсивной функции вычисления чисел Фибоначчи.  
В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и, если такие аргументы уже использовались, должен вернуть сохранённый результат вместо запуска расчёта.  

Советы  
- Для хранения результатов удобно использовать словарь, так как поиск элементов внутри словаря будет иметь сложность, равную в среднем O(1).  
- При этом не стоит хранить все вычисления в одном словаре, созданном снаружи функций (в глобальной области видимости). Лучше создавать  
 отдельные словари для каждой декорируемой функции.  

## Задача 4. Крестики нолики

Напишите программу, которая реализует игру Крестики-нолики.  
Ваши классы в этой задаче могут выглядеть так:  
```python
class Cell:
   #  Клетка, у которой есть значения
   #   - занята она или нет
   #   - номер клетки

class Board:
   #  Класс поля, который создаёт у себя экземпляры клетки

class Player:
   #  У игрока может быть
   #   - имя
   #   - на какую клетку ходит
```