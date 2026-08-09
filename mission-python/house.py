def main():
    name = input("Enter your name: ")
    #get house of the person (This is based on harry potter)
    print(house_name(name))

def house_name(person):
    # if person == "Harry" or person == "Ron" or person == "Hermione":
    #     return "Gryffindor"
    # elif person == "Draco":
    #     return "Slytherin"
    # else:
    #     return "Who?"

    # match-case
    # match person:
    #     case "Harry":
    #         house = "Gryffindor"
    #     case "Hermione":
    #         house = "Gryffindor"
    #     case "Ron":
    #         house = "Gryffindor"
    #     case "Draco":
    #         house = "Slytherin"
    #     case _:
    #         house = "Who?"

    #reduce case statements by using | (or) for simialar houses
    match person:
        case "Harry" | "Hermione" | "Ron":
            house = "Gryffindor"
        case "Draco":
            house = "Slytherin"
        case _:
            house = "Who?"

    return house

main()