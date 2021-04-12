# def selectsearch(arr):
    # for i in range(len(arr)-1):
    #     indexMin = i
    #     for k in range(i+1,len(arr)):
    #         if arr[k] < arr[indexMin]:
    #             indexMin = k
    #         else:
    #             k = k + 1
    #     w = arr[i]
    #     arr[i] = arr[indexMin]
    #     arr[indexMin] = w
    #     # arr[i], arr[indexMin] = arr[indexMin], arr[i] // 자리 바꾸기
    #     i = i + 1
    # return arr
                

array = [11,15,19,21,13,17]
# print(selectsearch(array))



for i in range(len(array)):
    w = array[i] # index 0 을 w 임시 최소값 설정
    indexMin = array.index(min(array[i:])) # array 안에 제일 작은 값을 indexMin 으로 설정
    array[i] = array[indexMin] # 제일 작은 값의 자리를 array[i]에 저장
    array[indexMin] = w #선택한 w 를 맨 뒤로 보낸다.

