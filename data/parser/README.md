## options
	- field : 필드명칭
	- measurement : measurement 명칭
	- dbname : 사용할 db 명칭
	- tags : tag_field1=tag_name1,tag_field2=tag_name2 형식으로 복수 입력 가능
	- time : data 삽입 시간
	- interval : time 시간 이후로 +interval 만큼 증가
	- input : csv 인풋 파일 path
	- dbid : 
	- dbpasswd : 

## 사용예시
	 - ./parser_csv_influx.py --field="acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z" --measurement="axis_data" --dbname="gesture_data" --tags="motion=front" --time=1485153595 --input=./front.dat --interval=100./parser_influx.py --field="acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z" --measurement="axis_data" --bname="gesture_data" --tags="motion=front" --time=1485153595 --input=./front.dat --interval=100
