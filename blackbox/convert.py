import os
  
files = os.listdir('murtazo/cloudnaca/msh/')
for file in files:
    if 'msh' in file:
        out = './mesh_xml/'+file.split('.')[0] + '.xml'
        os.system('dolfin-convert murtazo/cloudnaca/msh/'+file+' '+out)
