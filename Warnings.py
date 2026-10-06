#note to self. Don't name a python file 'warnings.py' Turns out that name is already taken and it's an important one
# could wrap this into a general matrix class maybe? Seems sensible tbh
def warnings(lightMatrix):
        if( lightMatrix[0][1] + lightMatrix[0][2] < 3):
            print(f"Your deck has only {lightMatrix[0][1] + lightMatrix[0][2]} bright exits")
        if( lightMatrix[1][0] + lightMatrix[1][2] < 3):
            print(f"Your deck has only {lightMatrix[0][1] + lightMatrix[0][2]} dim exits")
        if( lightMatrix[2][0] + lightMatrix[2][1] < 3):
            print(f"Your deck has only {lightMatrix[0][1] + lightMatrix[0][2]} dark exits")
    #Should be updated to add eclipse functionality!
