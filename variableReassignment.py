### Use this space to try out ideas and free code ###
i = -100
message_outside_loop = f"The variable i was {i} when I was defined outside the loop"
for i in range(0,5):
  message_inside_loop = f"The variable i was {i} when I was defined inside the loop"
  print(message_outside_loop)
  print(message_inside_loop, "\n====\n")
  
print("====Loop completed=====")
message_after_loops = f"The variable i is {i} now that the loop is done"
print(message_outside_loop)
print(message_inside_loop)
print(message_after_loops)