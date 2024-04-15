is_active = True
is_focus = False

if is_active and is_focus:
    print("very good")
elif not(is_active) and is_focus:
    print("not so good")
elif is_active and not(is_focus):
    print("good")   

else:
    print("not good")
