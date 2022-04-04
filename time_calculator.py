def add_time(start, duration, *args):
  [start_time, label] = start.split()
  [hstart_time, mstart_time] = start_time.split(":")
  [hduration, mduration] = duration.split(":")
  days = 0
  week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  minutes = int(mstart_time) + int(mduration)
  hours = int(hstart_time) + int(hduration)
  if minutes > 60:
    minutes -= 60
    hours += 1
  if minutes < 10:
    minutes = f"{minutes}".zfill(2)
  if hours >= 12:
    (t, r) = divmod(hours, 12)
  
    hours = r if r else hours
    if hours > 12:
      hours = hours - ((t-1) * 12)

  #if t > 0
    if label == "PM":
      days = ((t-1) // 2) + 1
    else:
      days = t // 2


    if t > 0 and t % 2 != 0:
      label = "AM" if label == "PM" else "PM"
  new_time = str(int(hours)) + ":"
  new_time += str(minutes) + f" {label}"

  if args:
    day = args[0].title()
    if days >= 1:
      index = week.index(day)
      index += days % 7
      if index > 6:
        index = index - 7
      day = week[index]
    new_time += f", {day}"
  if days == 1:
    new_time += "(next day)".rjust(11)
  elif days > 1:
    new_time += f" ({days} days later)".rjust(11)


  return new_time
