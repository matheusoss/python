
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

len(assistiram)

set(assistiram)

set([1,2,3,1])

{4, 1,2,3,1}

type({1,2})

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_machine_learning

usuarios_machine_learning[3]

for usuario in set(assistiram):
  print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_data_science | usuarios_machine_learning

usuarios_data_science & usuarios_machine_learning

usuarios_data_science - usuarios_machine_learning

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
15 in fez_ds_mas_nao_fez_ml

23 in fez_ds_mas_nao_fez_ml

usuarios_data_science ^ usuarios_machine_learning