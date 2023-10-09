import pytest

from Program import Program

# Инициализация списка 1
@pytest.fixture
def list1(): 
    return [1, 3, 5, 7, 9, 11, 13]

# Инициализация списка 2
@pytest.fixture
def list2(): 
    return [2, 4, 6, 8, 10, 12, 14]

#Проверка корректной инициализации
def testInit(l1, l2):
    numbersList = Program(l1, l2)
    assert numbersList.list1 == l1
    assert numbersList.list2 == l2

#Проверка средних значений списков размером больше 1
def testGetAverages(l1, l2):    
    numbersList = Program(l1, l2)
    assert numbersList.getAverages() == (7, 8)

#Проверка средних значений, если один или оба списка пустые
@pytest.mark.parametrize('l1, l2, res', [([1, 3, 5], [], (3, 0)), ([], [2, 4, 6], (0, 4)), ([], [], (0, 0))])
def testGetEmptyAverages(l1, l2, res):
    numbersList = Program(l1, l2)
    assert numbersList.getAverages() == res

#Проверка средних значений, если один или оба списка имеют только один элемент
@pytest.mark.parametrize('l1, l2, res', [([1, 4, 7], [9], (4, 9)), ([7], [9, 6, 3], (7, 6)), ([4], [4], (4, 4))])
def testGetElementAverages(l1, l2, res):
    numbersList = Program(l1, l2)
    assert numbersList.getAverages() == res

#Проверка сообщения когда среднее значение первого списка больше второго
def testFirstAverage(l1, l2, capfd):
    numbersList = Program(l2, l1)
    numbersList.compareAverages()
    capture = capfd.readouterr()
    assert capture.out.strip() == "Первый список имеет большее среднее значение"

#Проверка сообщения когда среднее значение второго списка больше первого
def test_second_average_more(l1, l2, capfd):
    numbersList = Program(l1, l2)
    numbersList.compareAverages()
    capture = capfd.readouterr()
    assert capture.out.strip() == "Второй список имеет большее среднее значение"

#Проверка сообщения когда средние значения списков равны
def test_equal_averages(l1, capfd):
    numbersList = Program(l1, list1)
    numbersList.compareAverages()
    capture = capfd.readouterr()
    assert capture.out.strip() == "Средние значения равны"