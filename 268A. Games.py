def count_games(n :int , teams:list[tuple]) -> int :
    """
    This is a function to count how many times the host team puts on the guest uniform 
    and this function uses brute force algorithm by trying all possible counts
    """
    count = 0 
    for i in range(n) : 
        home , guest = teams[i]
        for j in range(n) : 
            if i!=j :
                home2 , guest2 = teams[j]
                if guest2 == home : 
                    count+=1
    return count 

n = int(input())
teams = []
for i in range(n) : 
    #input = tuple(map(int,input().split()))
    team_input = tuple(map(int,input().split()))
    teams.append(team_input)
result = count_games(n,teams)
print(result)