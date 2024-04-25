def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(Name="Shivanand", Power="lazer", enemy = "Dr. Jackaal")
print_kwargs(Name="Shivanand")
