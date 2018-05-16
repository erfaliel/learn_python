#for generators with filter (multiple de 3 ici)
for i <- 1..20, rem(i, 3) == 0, do: i
