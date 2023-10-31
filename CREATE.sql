-- criar tabela autor
DROP TABLE IF EXISTS autor CASCADE ; 
CREATE TABLE autor ( 
	cod_autor				SMALLINT 		PRIMARY KEY, 
	nome_autor 				VARCHAR(50) 	NOT NULL, 
	pais_autor 				VARCHAR(50) 
); 

-- criar tabela situação
DROP TABLE IF EXISTS situacao CASCADE ; 
CREATE TABLE situacao ( 
	cod_situacao 			SMALLSERIAL 	PRIMARY KEY, 
	descr_situacao 			VARCHAR(100) 	NOT NULL 
); 

-- criar tabela tema
DROP TABLE IF EXISTS tema CASCADE ; 
CREATE TABLE tema ( 
	cod_tema 				SMALLSERIAL 	PRIMARY KEY, 
	descr_tema	 			VARCHAR(50) 	NOT NULL 
); 

-- criar tabela tipo_matricula
DROP TABLE IF EXISTS tipo_matricula CASCADE ; 
CREATE TABLE tipo_matricula ( 
	cod_tipo_matricula 		SMALLSERIAL 	PRIMARY KEY, 
	descr_tipo_matricula 	VARCHAR(100) 	NOT NULL 
); 

-- criar tabela instituicao
DROP TABLE IF EXISTS instituicao CASCADE ; 
CREATE TABLE instituicao ( 
	cod_instituicao 		SMALLSERIAL 	PRIMARY KEY, 
	nome_instituicao 		VARCHAR(100) 	NOT NULL, 
	endereco_instituicao	VARCHAR(500) 	NOT NULL, 
	etec_fatec 				CHAR(5) 		NOT NULL 
); 

-- criar tabela estante
/*
DROP TABLE IF EXISTS estante CASCADE ; 
CREATE TABLE estante ( 
	cod_estante 			SMALLSERIAL , 
	cod_instituicao			SMALLSERIAL 	REFERENCES instituicao(cod_instituicao) ,
	PRIMARY KEY (cod_estante, cod_instituicao)
); 
*/
DROP TABLE IF EXISTS estante CASCADE ; 
CREATE TABLE estante ( 
	cod_estante 			SMALLSERIAL 	PRIMARY KEY ,
	num_estante				SMALLINT ,
	cod_instituicao			SMALLSERIAL 	REFERENCES instituicao(cod_instituicao)
); 

-- criar tabela livro  
DROP TABLE IF EXISTS livro CASCADE ; 
CREATE TABLE livro ( 
	ISBN 					NUMERIC(10) 	PRIMARY KEY, 
	titulo 					VARCHAR(100) 	NOT NULL, 
	subtitulo 				VARCHAR(100) , 
	dt_publ 				DATE 			NOT NULL,  
	editora 				VARCHAR(50) 	NOT NULL,
	edicao 					SMALLINT,  
	local_publ 				VARCHAR(50) 
);  

-- criar tabela exemplar 
DROP TABLE IF EXISTS exemplar CASCADE ; 
CREATE TABLE exemplar ( 
	cod_exemplar 			SERIAL 			PRIMARY KEY,  
	ISBN 					NUMERIC(10) 	REFERENCES livro(ISBN),  
	dt_aquisicao 			DATE 			NOT NULL,  
--	cod_instituição			SMALLSERIAL 	REFERENCES estante(cod_instituicao), 
	cod_estante 			SMALLSERIAL		REFERENCES estante(cod_estante), 
	cod_situacao 			SMALLSERIAL 	NOT NULL 	REFERENCES situacao(cod_situacao), 
	estado_exemplar			CHAR(10) 		NOT NULL 
); 

-- criar tabela matricula
DROP TABLE IF EXISTS matricula CASCADE ; 
CREATE TABLE matricula ( 
	cod_matricula 			INTEGER 		PRIMARY KEY, 
	cod_tipo_matricula 		SMALLSERIAL 	NOT NULL 	REFERENCES tipo_matricula(cod_tipo_matricula),  
	cod_instituicao 		SMALLSERIAL  	REFERENCES instituicao(cod_instituicao), 
	nome_matricula 			VARCHAR(100) 	NOT NULL, 
	dt_matricula 			DATE 			NOT NULL, 
	sexo 					CHAR(1) 		NOT NULL, 
	dt_nscm 				DATE,  
	email_matricula 		VARCHAR(150),  
	endereco_matricula 		VARCHAR(500),  
	CPF						NUMERIC(11),  
	dt_termino 				DATE 
); 

-- criar tabela autoria
DROP TABLE IF EXISTS autoria CASCADE ; 
CREATE TABLE autoria ( 
	cod_autor 				SMALLSERIAL 	REFERENCES autor(cod_autor), 
	ISBN 					NUMERIC(10) 	REFERENCES livro(ISBN),
	PRIMARY KEY (cod_autor, ISBN)
);  

-- criar tabela classificacao
DROP TABLE IF EXISTS classificacao CASCADE ; 
CREATE TABLE classificacao ( 
	cod_tema	 			SMALLSERIAL 	REFERENCES tema(cod_tema) , 
	ISBN 					NUMERIC(10) 	REFERENCES livro(ISBN) ,
	PRIMARY KEY (cod_tema, ISBN)
); 

-- criar tabela reserva
DROP TABLE IF EXISTS reserva CASCADE ; 
CREATE TABLE reserva ( 
	cod_reserva				SERIAL			PRIMARY KEY,
	cod_matricula 			INTEGER 		REFERENCES matricula(cod_matricula), 
	cod_exemplar 			SMALLINT 		REFERENCES exemplar(cod_exemplar), 
	dt_reserva 				TIMESTAMP 		NOT NULL, 
	dt_prevista_emprestimo	DATE 			NOT NULL	CHECK (dt_prevista_emprestimo > dt_reserva),
	dt_emprestimo			DATE
); 

-- criar tabela emprestimo
DROP TABLE IF EXISTS emprestimo CASCADE ; 
CREATE TABLE emprestimo ( 
	cod_emprestimo			SERIAL			PRIMARY KEY,
	cod_matricula 			INTEGER 		REFERENCES matricula(cod_matricula), 
	cod_exemplar 			SMALLINT 		REFERENCES exemplar(cod_exemplar), 
	dt_emprestimo 			DATE	 		NOT NULL, 
	dt_prevista_devolucao 	DATE ,
	dt_devolucao 			DATE 
); 
