from rodents import Rodent

rodents={}
file=open('rodents.csv')
for line in file:
    line=line.rstrip()
    tag_id,weight=line.split(',')
    print tag_id
    tag_id,weight=line.split(",")
    if tag_id not in rodents:
        rodents[tag_id] = Rodent(tag_id)
        rodents[tag_id].add_weight(weight)
    else:
        rodents[tag_id].add_weight(weight)
file.close()
print rodents
for key in rodents:
    print rodents[key].tag_id, rodents[key].weights
