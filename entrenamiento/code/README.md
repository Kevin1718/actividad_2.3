# Instrucciones

## Imagen
```bash
docker build -t regresionlineal .
```

##Contenedor
```bash
docker run -it -p 8080:8080 -v "$PWD"/code/:/home/code/ --name gitpod_rl1 -h rl1 regresionlineal:v0.1
```