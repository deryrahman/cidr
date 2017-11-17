NIM="13515097"

run :
	printf "%s\n%s\n" $(NIM) $(NIM) | python src/client.py
