def combining_dict(my_dict1, my_dict2):
    my_dict1.update(my_dict2)
    return my_dict1
def main():
    team1 = {'John': 15, 'Lisa': 10, 'Mike': 12}
    team2 = {'Emily': 8, 'Chris': 20, 'Mike': 15}
    result = combining_dict(team1, team2)
    print(result)
main()
