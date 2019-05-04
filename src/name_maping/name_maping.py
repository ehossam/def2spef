
import json as json


# defFile = open('mux4x1_rows.def' , 'r' ) ;
out = open( 'mux4x1_rows.spef' , 'w' );

components = {}
nets  = {}
case = 0 ;
with open('mux4x1_rows.def') as myDef:
    for indx, line in enumerate(myDef) :
        if( case == 0 ):
            try:
                first = line.split()[0];
                second = line.split()[1];
                # print(first , case)
                if( first == "COMPONENTS" ):
                    case = 1 ;
                if ( first == "NETS" ) :
                    case = 2 ;

            except:
                pass
        # inside a case
        else:
            try:
                first = line.split()[0];
                second = line.split()[1];
                if( first == "END"):
                    case = 0 ;
                else:
                    if( case == 1 ):
                        components[second] = "+" ;
                    if( case == 2 and first == '-' ) :
                        nets[second] = "+" ;
                        # print('nets', second) ;
            except:
                pass

#name maping
out.write('*NAME_MAP \n');
out.write('\n')
cnt = 1
for key , value in components.items() :
    out.write("*" + str(cnt) + " " + key + "\n" );
    cnt+=1

for key , value in nets.items() :
    out.write("*" + str(cnt) + " " + key + "\n" );
    cnt+=1;

print(nets)
print(components)