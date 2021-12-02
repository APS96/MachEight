def height_func(players,input_height):
    result=""
    if not str.isdigit(input_height):
        result="Input not Integer"
        print(result)
        return result
    if input_height=="0" or input_height==0:
        result="Input is 0"
        print(result)
        return result
    
    input_height_int=int(input_height)
    pair_list=[]
    
    max_h=0
    min_h=1000000000000
    #O(n^2)
    for i in range(len(players)):
        player=players[i]
        complement=str(input_height_int-int(player['h_in']))
        if max_h<int(player['h_in']):
            max_h=int(player['h_in'])
        if min_h>int(player['h_in']):
            min_h=int(player['h_in'])
        for player2 in players[i:]:
            if player!=player2 and player2['h_in']==complement:
                #pair=f"- {player['first_name']} {player['last_name']}         {player2['first_name']} {player2['last_name']}"
                pair=prettyPrint(player['first_name'],player['last_name'],player2['first_name'],player2['last_name'],22)
                print(pair)
                pair_list.append(pair)
    if len(pair_list)==0:
        result="No matches found"
        max_height_pair=max_h*2
        min_height_pair=min_h*2
        if input_height_int>max_height_pair:
            result=result+". Try an input smaller than "+str(max_height_pair)+" since the most tall player measures "+str(max_h) +" inches."
        if input_height_int<min_height_pair:
            result=result+". Try an input larger than "+str(min_height_pair)+" since the least tall player measures "+str(min_h) +" inches."
        print(result)
        return result
    return pair_list

def prettyPrint(player1_Name,player1_LastName,player2_Name,player2_LastName,spaces):
    return f"- {player1_Name} {player1_LastName}"+(' ' * (spaces-len(player1_Name+" "+player1_LastName)))+f"{player2_Name} {player2_LastName}"