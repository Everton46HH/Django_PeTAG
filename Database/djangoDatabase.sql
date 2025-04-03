	drop database if exists PeTAG;
	create database PeTAG;
	use PeTAG;

	create table Usuario(
		userID INT AUTO_INCREMENT primary key,
		nome varchar(40),
		email varchar(40),
		senha varchar(40),
		telefone varchar(40)
	);

	create table Dispositivo(
		idDispositivo INT AUTO_INCREMENT primary key,
		nomeDispositivo varchar(40),
		longitude float(20),
		latitude float(20)
	);

	create table HistoricoCoordenadas (
	idHistorico INT AUTO_INCREMENT PRIMARY KEY,
	idDispositivo INT,
	latitude FLOAT(20),
	longitude FLOAT(20),
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (idDispositivo) REFERENCES Dispositivo(idDispositivo)
	);

	INSERT INTO Usuario (userID, nome, email, senha,telefone) 
	VALUES 
	(1, 'João', 'joao@gmail.com', 'senha123','4022-8922');

	INSERT INTO Dispositivo	 (idDispositivo,nomeDispositivo, latitude, longitude) 
	VALUES 
	(1,'Rex', 0, 0);

	update Dispositivo set latitude = -22.8880, longitude = -46.4136 where idDispositivo = 1;
    update Dispositivo set latitude = 48.85286423416817 , longitude = 2.370712607481553 where idDispositivo = 1;
	update Dispositivo set latitude = 0 , longitude = 0 where idDispositivo = 1;
	COMMIT;
    
    
	select * from Usuario;
    select * from Dispositivo;
    select * from HistoricoCoordenadas	;