-- criar tabela autor
DROP TABLE IF EXISTS autor CASCADE ; 
CREATE TABLE autor ( 
	cod_autor				SMALLINT 		PRIMARY KEY, 
	nome_autor 				VARCHAR(50) 	NOT NULL, 
	pais_autor 				VARCHAR(50) 
); 
-- Populando autor
INSERT INTO autor (cod_autor,nome_autor,pais_autor)
	VALUES
	(1,'Robert C. Martin ','Estados Unidos'),
	(2,'Andrew Hunt','Inglaterra'),
	(3,'David Thomas','Inglaterra'),
	(4,'Yuval Noah Harari','Israel'),
	(5,'Walter Isaacson','Estados Unidos'),
	(6,'Eric Matthes','Estados Unidos'),
	(7,'Erich Gamma','Suiça'),
	(8,'Richard Helm','Estados Unidos'),
	(9,'Ralph Johnson','Estados Unidos'),
	(10,'Gene Kim','Estados Unidos'),
	(11,'Kevin Behr','Estados Unidos'),
	(12,'George Spafford','Estados Unidos'),
	(13,'Karina Vazquez','Brasil'),
	(14,'Mark Manson','Estados Unidos'),
	(15,'Andreas M. Antonopoulos','Grécia'),
	(16,'Charles Duhigg','Mexico'),
	(17,'Timothy Ferriss','Estados Unidos'),
	(18,'Carol S. Dweck ','Estados Unidos'),
	(19,'Robert T. Kiyosaki','Estados Unidos');


-- criar tabela situação
DROP TABLE IF EXISTS situacao CASCADE ; 
CREATE TABLE situacao ( 
	cod_situacao 			SMALLSERIAL 	PRIMARY KEY, 
	descr_situacao 			VARCHAR(100) 	NOT NULL 
); 
-- Populando situação
INSERT INTO situacao (cod_situacao,descr_situacao)
	VALUES
	(1,'Disponível'),
	(2,'Emprestado'),
	(3,'Reparo/Manutenção'),
	(4,'Perdido');


-- criar tabela tema
DROP TABLE IF EXISTS tema CASCADE ; 
CREATE TABLE tema ( 
	cod_tema 				SMALLSERIAL 	PRIMARY KEY, 
	descr_tema	 			VARCHAR(50) 	NOT NULL 
); 
-- Populando Tema
INSERT INTO tema (cod_tema, descr_tema)
	VALUES
	(1,'Blockchain'),
	(2,'Boas práticas de codificação'),
	(3,'Criptomoedas'),
	(4,'Desenvolvimento de software'),
	(5,'Desenvolvimento pessoal'),
	(6,'DevOps'),
	(7,'Dicas'),
	(8,'Educação financeira'),
	(9,'Engenharia de software'),
	(10,'Finanças pessoais'),
	(11,'Hábitos'),
	(12,'História da humanidade e da civilização'),
	(13,'História da tecnologia e inovação'),
	(14,'Inteligência artificial e suas aplicações'),
	(15,'Introdução à programação'),
	(16,'Investimentos'),
	(17,'Mudança comportamental'),
	(18,'Padrões de design'),
	(19,'Programação'),
	(20,'Programação em Python'),
	(21,'Psicologia positiva'),
	(22,'Técnicas para programadores'),
	(23,'Tecnologia financeira'),
	(24,'Tecnologia da informação');


-- criar tabela tipo_matricula
DROP TABLE IF EXISTS tipo_matricula CASCADE ; 
CREATE TABLE tipo_matricula ( 
	cod_tipo_matricula 		SMALLSERIAL 	PRIMARY KEY, 
	descr_tipo_matricula 	VARCHAR(100) 	NOT NULL 
); 
-- Populando tipo_matricula
INSERT INTO tipo_matricula (cod_tipo_matricula,descr_tipo_matricula)
	VALUES
	(1,'Estudante'),
	(2,'Professor'),
	(3,'Funcionário'),
	(4,'Externo');
 

-- criar tabela instituicao
DROP TABLE IF EXISTS instituicao CASCADE ; 
CREATE TABLE instituicao ( 
	cod_instituicao 		SMALLSERIAL 	PRIMARY KEY, 
	nome_instituicao 		VARCHAR(100) 	NOT NULL, 
	endereco_instituicao	VARCHAR(500) 	NOT NULL, 
	etec_fatec 				CHAR(5) 		NOT NULL 
); 
--Populando instituicao
INSERT INTO instituicao (cod_instituicao, nome_instituicao, endereco_instituicao, etec_fatec)
	VALUES
	(1, 'Fatec Sao Paulo', 'Av. Tiradentes, 615 - Bom Retiro - Sao Paulo/SP', 'Fatec'),
	(2, 'Fatec Pastor Eneas Tognini', 'R. Frei João, 59 - Vila Nair - Sao Paulo/SP', 'Fatec'), 
	(3, 'Fatec SEBRAE', 'Alameda Nothman 598 - Campos Eliseos - Sao Paulo/SP', 'Fatec'),
	(4, 'Etec Getulio Vargas', 'Rua Moreira e Costa, 243 - Ipiranga - Sao Paulo/SP', 'Etec'),
	(5, 'Etec Lauro Gomes', 'Av. Pereira Barreto, 400 - Vila Baeta Neves - Sao Bernardo do Campo/SP', 'Etec');


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
--Populando Estante
INSERT INTO estante (num_estante, cod_instituicao)
	VALUES
	(1, 1),
	(2, 1),
	(3, 1),
	(4, 1),
	(5, 1),
	(1, 2),
	(2, 2),
	(3, 2),
	(4, 2),
	(5, 2),
	(1, 3),
	(2, 3),
	(3, 3),
	(4, 3),
	(5, 3),
	(1, 4),
	(2, 4),
	(3, 4),
	(4, 4),
	(5, 4),
	(1, 5),
	(2, 5),
	(3, 5),
	(4, 5),
	(5, 5);


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
--Populando Livro
INSERT INTO livro (ISBN, titulo, subtitulo, dt_publ, editora, edicao, local_publ)
	VALUES
	(0132350884, 'Clean Code', 'A Handbook of Agile Software Craftsmanship', '2008-08-11', 'Prentice Hall', 1, 'Nova York, EUA'),
	(0137081073, 'The Clean Coder', 'A Code of Conduct for Professional Programmers', '2011-05-23', 'Prentice Hall', 1, 'Nova York, EUA'),
	(0201616224, 'The Pragmatic Programmer', 'Your Journey to Mastery', '1999-10-20', 'Addison-Wesley Professional', 1, 'Boston, EUA'),
	(0201734843, 'Pragmatic Unit Testing in Java with JUnit', NULL, '2003-09-08', 'Addison-Wesley Professional', 1, 'Boston, EUA'),
	(0062316110, 'Sapiens: A Brief History of Humankind', NULL, '2015-02-10', 'Harper', 1, 'Nova York, EUA'),
	(0062464316, 'Homo Deus: A Brief History of Tomorrow', NULL, '2017-02-21', 'Harper', 1, 'Nova York, EUA'),
	(0743264730, 'Benjamin Franklin: An American Life', NULL, '2003-07-04', 'Simon & Schuster', 1, 'Nova York, EUA'),
	(1501127620, 'Steve Jobs', NULL, '2011-10-24', 'Simon & Schuster', 1, 'Nova York, EUA'),
	(1593276034, 'Python Crash Course', 'A Hands-On, Project-Based Introduction to Programming', '2015-11-20', 'No Starch Press', 1, 'São Francisco, EUA'),
	(1593279912, 'Python Crash Course', 'A Hands-On, Project-Based Introduction to Programming', '2019-05-08', 'No Starch Press', 2, 'São Francisco, EUA'),
	(0201633610, 'Design Patterns', 'Elements of Reusable Object-Oriented Software', '1994-10-31', 'Addison-Wesley Professional', 1, 'Boston, EUA'),
	(1942788003, 'The Phoenix Project', 'A Novel About IT, DevOps, and Helping Your Business Win', '2013-01-10', 'IT Revolution Press', 1, 'Portland, EUA'),
	(0062457714, 'The Subtle Art of Not Giving a F*ck', 'A Counterintuitive Approach to Living a Good Life', '2016-09-13', 'HarperOne', 1, 'Nova York, EUA'),
	(0062885422, 'Everything Is F*cked', 'A Book About Hope', '2019-05-14', 'Harper', 1, 'Nova York, EUA'),
	(1491954386, 'Mastering Bitcoin', 'Unlocking Digital Cryptocurrencies', '2014-12-24', 'O´Reilly Media', 1, 'California, EUA'),
	(1491904240, 'Mastering Ethereum', 'Building Smart Contracts and DApps', '2018-12-02', 'O´Reilly Media', 1, 'California, EUA'),
	(1400069286, 'The Power of Habit', 'Why We Do What We Do in Life and Business', '2012-02-28', 'Random House', 1, 'Nova York, EUA'),
	(0812981605, 'Smarter Faster Better', 'The Secrets of Being Productive in Life and Business', '2016-03-08', 'Random House', 1, 'Nova York, EUA'),
	(0307465351, 'The 4-Hour Workweek', 'Escape 9-5, Live Anywhere, and Join the New Rich', '2007-04-24', 'Harmony', 1, 'Nova York, EUA'),
	(0307463630, 'The 4-Hour Body', 'An Uncommon Guide to Rapid Fat-Loss, Incredible Sex, and Becoming Superhuman', '2010-12-14', 'Harmony', 1, 'Nova York, EUA'),
	(0345472328, 'Mindset: The New Psychology of Success', NULL, '2006-12-26', 'Random House', 1, 'Nova York, EUA'), 
	(0345805852, 'Self-Theories: Their Role in Motivation, Personality, and Development', NULL, '1999-07-27', 'Psychology Press', 1, 'Nova York, EUA'),
	(0446677455, 'Rich Dad Poor Dad', 'What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!', '1997-06-19', 'Plata Publishing', 2, 'Arizona, EUA'),
	(1612680170, 'Cashflow Quadrant', 'Rich Dad´s Guide to Financial Freedom', '2000-01-01', 'Plata Publishing', 1, 'Arizona, EUA');


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
-- Populando Exemplar
INSERT INTO exemplar (ISBN, dt_aquisicao, cod_estante, cod_situacao, estado_exemplar)
	VALUES
	(0132350884, '2023-10-22', 1, 1, 'Preservado'),
	(0132350884, '2023-2-22', 1, 1, 'Danificado'),
	(0132350884, '2023-10-22', 1, 1, 'Preservado'),
	(0137081073, '2019-12-14', 2, 4, 'Danificado'),
	(1491904240, '2018-4-1', 1, 3, 'Preservado'),
	(1491904240, '2020-4-10', 1, 1, 'Preservado'),
	(0345805852, '2018-10-26', 3, 1, 'Danificado'),
	(0307463630, '2020-6-14', 10, 1, 'Preservado'),
	(0307463630, '2018-1-24', 1, 1, 'Preservado'),
	(0307463630, '2019-2-24', 5, 1, 'Preservado'),
	(0201734843, '2014-3-21', 18, 2, 'Preservado'),
	(0201734843, '2014-4-21', 17, 3, 'Danificado'),
	(0201734843, '2013-5-15', 14, 4, 'Preservado'),
	(0062457714, '2018-6-17', 15, 2, 'Preservado'),
	(0062457714, '2019-7-19', 18, 1, 'Danificado'),
	(0062457714, '2018-8-29', 19, 1, 'Preservado'),
	(0446677455, '2018-9-30', 1, 1, 'Danificado'),
	(0446677455, '2017-10-24', 9, 3, 'Preservado'),
	(0446677455, '2015-11-25', 19, 4, 'Danificado'),
	(0062464316, '2018-12-20', 8, 3, 'Preservado'),
	(0062464316, '2021-1-20', 9, 1, 'Preservado'),
	(0062464316, '2020-1-10', 6, 1, 'Preservado'),
	(0201616224, '2020-1-19', 5, 1, 'Preservado'),
	(0201616224, '2018-12-18', 8, 1, 'Danificado'),
	(0201616224, '2017-2-1', 7, 1, 'Preservado'),
	(0201616224, '2018-2-15', 5, 1, 'Danificado'),
	(0345472328, '2019-2-5', 6, 1, 'Preservado'),
	(0345472328, '2020-2-9', 5, 4, 'Preservado'),
	(0345472328, '2021-3-7', 4, 3, 'Danificado'),
	(0345472328, '2021-5-4', 8, 1, 'Preservado'),
	(0132350884, '2022-5-5', 7, 3, 'Preservado'),
	(0132350884, '2019-4-4', 24, 4, 'Danificado'),
	(0132350884, '2019-4-9', 8, 4, 'Preservado'),
	(1942788003, '2018-7-6', 25, 1, 'Danificado'),
	(1942788003, '2018-8-5', 23, 1, 'Preservado'),
	(1942788003, '2017-8-4', 23, 3, 'Danificado'),
	(0345472328, '2017-8-7', 22, 4, 'Preservado'),
	(0345472328, '2019-7-8', 21, 4, 'Danificado'),
	(0345472328, '2019-7-9', 21, 3, 'Danificado'),
	(0446677455, '2020-4-1', 20, 4, 'Preservado'),
	(0446677455, '2022-9-2', 10, 1, 'Preservado'),
	(0201633610, '2021-5-15', 10, 1, 'Preservado'),
	(1593276034, '2022-6-18', 16, 1, 'Preservado'),
	(1942788003, '2020-6-19', 15, 1, 'Preservado'),
	(0062457714, '2017-4-5', 14, 1, 'Preservado'),
	(0062885422, '2019-4-7', 14, 1, 'Danificado'),
	(1491954386, '2018-8-9', 18, 1, 'Preservado'),
	(1491904240, '2017-4-6', 17, 1, 'Preservado'),
	(1400069286, '2018-2-26', 19, 1, 'Danificado'),
	(0812981605, '2019-1-22', 15, 1, 'Preservado'),
	(0345472328, '2019-5-21', 12, 3, 'Preservado');


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
--Populando matricula
INSERT INTO matricula(cod_matricula, cod_tipo_matricula, cod_instituicao, nome_matricula, dt_matricula, sexo, dt_nscm, email_matricula, endereco_matricula, CPF, dt_termino)
	VALUES
	(40101, 1, 1, 'Maria da Silva', '2022-02-10', 'F', '2005-05-15', 'maria.silva@example.com', 'Rua da Universidade, 123 - Vila Cursinho - São Paulo/SP', 12345678909, '2025-11-30'),
	(40111, 1, 1, 'João Oliveira', '2021-07-20', 'M', '1997-12-03', 'joao.oliveira@studentmail.com', 'Avenida dos Estudantes, 45 - Campos Concurso - São Paulo/SP - São Paulo/SP', 98765432102, '2024-06-30'),
	(40102, 1, 2, 'Ana Santos', '2022-01-05', 'F', '1999-08-22', 'ana.santos@universitymail.com', 'Travessa do Ensino, 07 - Vila Saber - São Paulo/SP', 32165498740, '2024-12-30'),
	(40121, 1, 1, 'Pedro Pereira', '2021-03-12', 'M', '1998-02-10', 'pedro.pereira@example.com', 'Rua dos Estudantes, 56 - Campo Novo - São Paulo/SP', 13246579887, '2023-11-30'),
	(40103, 1, 3, 'Sofia Rodrigues', '2022-08-30', 'F', '1997-11-05', 'sofia.rodrigues@studentmail.com', 'Alameda da Escola, 89 - Bairro do Intercâmbio - São Paulo/SP', 31264597819, '2025-07-30'),
	(40113, 1, 3, 'Lucas Fernandes', '2021-05-05', 'M', '1996-09-30', 'lucas.fernandes@universitymail.com', 'Praça do Conhecimento, 12 - Campo da Concórdia - São Paulo/SP', 96385274101, '2024-05-30'),
	(40112, 1, 2, 'Carlos Lima', '2021-12-18', 'M', '1999-03-18', 'carlos.lima@example.com', 'Rua dos Alunos, 67 - Avenida dos Professores - São Paulo/SP', 74185296321, '2024-10-30'),
	(40122, 1, 2, 'Beatriz Costa', '2021-06-02', 'F', '1997-07-12', 'beatriz.costa@studentmail.com', 'Alameda das Lições, 21 - Bairro do Livro - São Paulo/SP', 85296314742, '2024-04-30'),
	(40123, 1, 3, 'Rafaela Vieira', '2022-02-15', 'F', '1998-01-25', 'rafaela.vieira@universitymail.com', 'Avenida da Educação, 34 - Praça do Bom Progresso - São Paulo/SP', 15923647813, '2025-09-30'),
	(40131, 1, 1, 'Felipe Santos', '2021-10-25', 'M', '1996-10-09', 'felipe.santos@example.com', 'Travessa dos Estudantes, 03 - Campo do Sucesso - São Paulo/SP', 87495163285, '2024-08-30'),
	(40104, 1, 4, 'Luana Almeida', '2022-03-01', 'F', '2005-05-22', 'luana.almeida@example.com', 'Rua do Colégio, 123 - Vila da Apostila - São Paulo/SP', 14523697825, '2025-11-30'),
	(40105, 1, 5, 'Gustavo Martins', '2021-08-15', 'M', '2024-12-03', 'gustavo.martins@studentmail.com', 'Avenida dos Estudantes, 45 - Vila do Aprendizado - São Bernardo do Campo/SP', 15395748629, '2024-06-30'),
	(40115, 1, 5, 'Júlia Ferreira', '2022-02-05', 'F', '2006-08-22', 'julia.ferreira@universitymail.com', 'Rua da Educação, 75 - Nova História - São Bernardo do Campo/SP', 84286273964, '2024-12-30'),
	(40114, 1, 4, 'Eduardo Lima', '2021-04-12', 'M', '2005-02-10', 'eduardo.lima@example.com', 'Alameda do Ensino, 994 - Largo da Moral - São Paulo/SP', 30124180907, '2023-11-30'),
	(40124, 1, 4, 'Mariana Costa', '2022-09-20', 'F', '2004-11-05', 'mariana.costa@studentmail.com', 'Ladeira da Escola, 452 - Vila Esperança - São Paulo/SP', 90584420132, '2025-07-30'),
	(40134, 1, 4, 'Gabriel Oliveira', '2021-06-03', 'M', '2003-09-30', 'gabriel.oliveira@universitymail.com', 'Rua da Lição, 847 - Vila da Biblioteca - São Paulo/SP', 99039389793, '2024-05-30'),
	(40125, 1, 5, 'Isabela Teixeira', '2022-01-12', 'F', '2006-04-07', 'isabela.teixeira@example.com', 'Travessa do Curso, 951 - Campo da Razão - São Bernardo do Campo/SP', 45065443252, '2024-10-30'),
	(40135, 1, 5, 'Rafael Silva', '2021-07-22', 'M', '2004-07-12', 'rafael.silva@studentmail.com', 'Rua da Matéria, 865 - Campo da Faculdade - São Bernardo do Campo/SP', 35065420174, '2024-04-30'),
	(40141, 1, 2, 'Fernanda Santos', '2022-04-15', 'F', '1999-06-25', 'fernanda.santos@example.com', 'Rua das Aulas, 87 - Vila do Saber - São Paulo/SP', 98765432109, '2024-12-30'),
	(40151, 1, 3, 'Rodrigo Fernandes', '2021-11-10', 'M', '1997-09-14', 'rodrigo.fernandes@studentmail.com', 'Avenida da Ciência, 56 - Bairro do Conhecimento - São Paulo/SP', 12345678912, '2024-05-30'),
	(40142, 1, 4, 'Camila Lima', '2022-07-02', 'F', '1998-03-18', 'camila.lima@example.com', 'Rua dos Livros, 67 - Praça dos Professores - São Paulo/SP', 74185296327, '2024-10-30'),
	(40152, 1, 5, 'Felipe Costa', '2021-09-22', 'M', '1996-08-10', 'felipe.costa@example.com', 'Travessa das Lições, 32 - Avenida dos Estudantes - São Bernardo do Campo/SP', 85296314755, '2024-04-30'),
	(40143, 1, 2, 'Carolina Oliveira', '2022-05-30', 'F', '1997-11-05', 'carolina.oliveira@studentmail.com', 'Alameda do Saber, 89 - Bairro do Estudo - São Paulo/SP', 31264597821, '2025-07-30'),
	(40153, 1, 3, 'Miguel Rodrigues', '2021-08-10', 'M', '1996-02-25', 'miguel.rodrigues@universitymail.com', 'Rua da Aprendizagem, 54 - Campo do Saber - São Paulo/SP', 15923647817, '2024-09-30'),
	(40144, 1, 4, 'Evelyn Almeida', '2022-02-18', 'F', '2005-05-22', 'evelyn.almeida@example.com', 'Alameda das Apostilas, 123 - Vila da Leitura - São Paulo/SP', 14523697829, '2025-11-30'),
	(40154, 1, 5, 'Rafael Martins', '2021-06-15', 'M', '2004-12-03', 'rafael.martins@studentmail.com', 'Avenida dos Conhecimentos, 45 - Vila do Aprendizado - São Bernardo do Campo/SP', 15395748632, '2024-06-30'),
	(40145, 1, 2, 'Amanda Ferreira', '2022-01-10', 'F', '2006-08-22', 'amanda.ferreira@universitymail.com', 'Rua da Sabedoria, 75 - Nova Leitura - São Paulo/SP', 84286273968, '2024-12-30'),
	(40155, 1, 3, 'Lucas Lima', '2021-04-25', 'M', '2005-02-10', 'lucas.lima@example.com', 'Alameda do Conhecimento, 994 - Largo do Progresso - São Paulo/SP', 30124180912, '2023-11-30'),
	(40146, 1, 4, 'Juliana Costa', '2022-10-20', 'F', '2004-11-05', 'juliana.costa@studentmail.com', 'Ladeira do Estudo, 452 - Vila Esperança - São Paulo/SP', 90584420135, '2025-07-30'),
	(40156, 1, 4, 'Renan Oliveira', '2021-07-03', 'M', '2003-09-30', 'renan.oliveira@universitymail.com', 'Rua da Sabedoria, 847 - Vila da Leitura - São Paulo/SP', 99039389799, '2024-05-30'),
	(40147, 1, 5, 'Bianca Teixeira', '2022-03-12', 'F', '2006-04-07', 'bianca.teixeira@example.com', 'Travessa das Lições, 951 - Campo do Aprendizado - São Bernardo do Campo/SP', 45065443259, '2024-10-30'),
	(40157, 1, 5, 'Gustavo Silva', '2021-09-30', 'M', '2004-07-12', 'gustavo.silva@studentmail.com', 'Rua do Progresso, 865 - Vila da Educação - São Bernardo do Campo/SP', 35065420179, '2024-04-30'),
	(40148, 1, 2, 'Isadora Santos', '2022-02-25', 'F', '1998-01-25', 'isadora.santos@universitymail.com', 'Avenida da Sabedoria, 34 - Praça do Conhecimento - São Paulo/SP', 15923647821, '2025-09-30'),
	(40158, 1, 2, 'Henrique Pereira', '2021-06-18', 'M', '1999-03-18', 'henrique.pereira@example.com', 'Rua dos Alunos, 67 - Avenida dos Professores - São Paulo/SP', 74185296330, '2024-10-30'),
	(40149, 1, 3, 'Larissa Vieira', '2022-03-05', 'F', '1998-01-25', 'larissa.vieira@universitymail.com', 'Alameda da Educação, 34 - Praça do Bom Progresso - São Paulo/SP', 15923647823, '2025-09-30');


-- criar tabela autoria
DROP TABLE IF EXISTS autoria CASCADE ; 
CREATE TABLE autoria ( 
	cod_autor 				SMALLSERIAL 	REFERENCES autor(cod_autor), 
	ISBN 					NUMERIC(10) 	REFERENCES livro(ISBN),
	PRIMARY KEY (cod_autor, ISBN)
);  
--Populando Autoria
INSERT INTO autoria (cod_autor, ISBN)
	VALUES
	(1, 0132350884),
	(1, 0137081073),
	(2, 0201616224),
	(3, 0201616224),
	(2, 0201734843),
	(3, 0201734843),
	(4, 0062316110),
	(4, 0062464316),
	(5, 0743264730), 
	(5, 1501127620),
	(6, 1593276034),
	(6, 1593279912), 
	(7, 0201633610),
	(8, 0201633610),
	(9, 0201633610),
	(10, 1942788003),
	(11, 1942788003),
	(12, 1942788003),
	(14, 0062457714),
	(14, 0062885422),
	(15, 1491954386),
	(15, 1491904240),
	(16, 1400069286),
	(16, 0812981605),
	(17, 0307465351),
	(17, 0307463630),
	(18, 0345472328), 
	(18, 0345805852),
	(19, 0446677455),
	(19, 1612680170);


-- criar tabela classificacao
DROP TABLE IF EXISTS classificacao CASCADE ; 
CREATE TABLE classificacao ( 
	cod_tema	 			SMALLSERIAL 	REFERENCES tema(cod_tema) , 
	ISBN 					NUMERIC(10) 	REFERENCES livro(ISBN) ,
	PRIMARY KEY (cod_tema, ISBN)
); 
--Populando classificacao
INSERT INTO classificacao (ISBN, cod_tema)
	VALUES
	(0132350884, 2),
	(0132350884, 19),
	(0132350884, 22),
	(0137081073, 2),
	(0137081073, 19),
	(0137081073, 22),
	(0201616224, 2),
	(0201616224, 19),
	(0201616224, 22),
	(0201734843, 2),
	(0201734843, 19),
	(0201734843, 22),
	(0062316110, 12),
	(0062464316, 12),
	(0743264730, 12),
	(1501127620, 13),
	(1593276034, 15),
	(1593276034, 19),
	(1593276034, 20),
	(1593276034, 22),
	(1593279912, 15),
	(1593279912, 19),
	(1593279912, 20),
	(1593279912, 22),
	(0201633610, 9),
	(0201633610, 4),
	(0201633610, 19),
	(1942788003, 6),
	(1942788003, 7),
	(1942788003, 24),
	(0062457714, 7),
	(0062457714, 5),
	(0062457714, 17),
	(0062885422, 5),
	(0062885422, 7),
	(0062885422, 17),
	(0062885422, 21),
	(1491954386, 3),
	(1491954386, 10),
	(1491954386, 16),
	(1491954386, 23),
	(1491904240, 3),
	(1491904240, 10),
	(1491904240, 16),
	(1491904240, 23),
	(1400069286, 11),
	(1400069286, 7),
	(1400069286, 5),
	(0812981605, 5),
	(0812981605, 7),
	(0812981605, 11),
	(0812981605, 17),
	(0307465351, 11),
	(0307465351, 17),
	(0307463630, 11),
	(0307463630, 17),
	(0307463630, 7),
	(0345472328, 5),
	(0345472328, 21),
	(0345805852, 5),
	(0345805852, 7),
	(0345805852, 21),
	(0446677455, 8),
	(0446677455, 10),
	(0446677455, 11),
	(1612680170, 8),
	(1612680170, 10),
	(1612680170, 23);


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
-- Populando reserva
INSERT INTO reserva (cod_reserva, cod_matricula, cod_exemplar, dt_reserva, dt_prevista_emprestimo, dt_emprestimo)
        VALUES
	(1, 40101, 1, '2022-12-15', '2022-12-18', '2022-12-17'),
	(2, 40102, 2, '2021-11-28', '2021-12-01', '2021-12-01'),
	(3, 40103, 3, '2021-11-05', '2021-11-08', '2021-11-08'),
	(4, 40104, 4, '2022-10-10', '2022-10-13', '2022-10-12'),
	(5, 40105, 5, '2022-03-07', '2022-03-10', '2022-03-09'),
	(6, 40105, 6, '2021-09-22', '2021-09-25', '2021-09-25'),
	(7, 40103, 7, '2022-08-15', '2022-08-18', '2022-08-17'),
	(8, 40158, 8, '2021-07-01', '2021-07-04', '2021-07-04'),
	(9, 40147, 9, '2022-01-20', '2022-01-23', '2022-01-22'),
	(10, 40103, 10, '2022-06-12', '2022-06-15', '2022-06-14'),
	(11, 40111, 11, '2021-05-28', '2021-05-31', '2021-05-31'),
	(12, 40112, 12, '2022-04-02', '2022-04-05', '2022-04-04'),
	(13, 40113, 13, '2022-02-17', '2022-02-20', '2022-02-19'),
	(14, 40114, 14, '2021-11-10', '2021-11-13', '2021-11-13'),
	(15, 40115, 15, '2021-09-05', '2021-09-08', '2021-09-08'),
	(16, 40146, 16, '2022-07-14', '2022-07-17', '2022-07-16'),
	(17, 40147, 17, '2021-12-30', '2022-01-02', '2022-01-01'),
	(18, 40158, 18, '2022-03-24', '2022-03-27', '2022-03-26'),
	(19, 40145, 19, '2022-05-19', '2022-05-22', '2022-05-21'),
	(20, 40142, 1, '2021-08-09', '2021-08-12', '2021-08-12'),
	(21, 40121, 16, '2022-06-18', '2022-06-21', '2022-06-20'),
	(22, 40122, 18, '2021-11-01', '2021-11-04', '2021-11-03'),
	(23, 40123, 19, '2021-10-05', '2021-10-08', '2021-10-07'),
	(24, 40124, 3, '2022-11-10', '2022-11-13', '2022-11-12'),
	(25, 40125, 5, '2022-04-07', '2022-04-10', '2022-04-09'),
	(26, 40143, 6, '2021-10-22', '2021-10-25', '2021-10-24'),
	(27, 40147, 17, '2022-09-15', '2022-09-18', '2022-09-17'),
	(28, 40146, 12, '2021-08-01', '2021-08-04', '2021-08-04'),
	(29, 40141, 8, '2022-02-10', '2022-02-13', '2022-02-12'),
	(30, 40101, 2, '2022-06-02', '2022-06-05', '2022-06-04'),
	(31, 40131, 13, '2023-02-15', '2023-02-18', '2023-02-17'),
	(32, 40104, 7, '2023-04-05', '2023-04-08', '2023-04-07'),
	(33, 40105, 11, '2023-06-20', '2023-06-23', '2023-06-22'),
	(34, 40134, 16, '2023-08-12', '2023-08-15', '2023-08-14'),
	(35, 40135, 19, '2023-10-10', '2023-10-13', '2023-10-12'),
	(36, 40101, 1, '2023-12-18', '2023-12-21', '2023-12-20'),
	(37, 40102, 2, '2022-11-28', '2022-12-01', '2022-12-01'),
	(38, 40103, 3, '2022-11-05', '2022-11-08', '2022-11-08'),
	(39, 40104, 4, '2023-10-10', '2023-10-13', '2023-10-12'),
	(40, 40105, 5, '2023-03-07', '2023-03-10', '2023-03-09'),
	(41, 40104, 6, '2023-09-22', '2023-09-25', '2023-09-25'),
	(42, 40103, 7, '2022-08-15', '2022-08-18', '2022-08-17'),
	(43, 40158, 8, '2023-01-01', '2023-01-04', '2023-01-03'),
	(44, 40147, 9, '2023-05-20', '2023-05-23', '2023-05-22'),
	(45, 40103, 10, '2022-06-12', '2022-06-15', '2022-06-14'),
	(46, 40111, 11, '2022-03-28', '2022-03-31', '2022-03-31'),
	(47, 40112, 12, '2023-03-15', '2023-03-18', '2023-03-17'),
	(48, 40113, 13, '2021-12-22', '2021-12-25', '2021-12-24'),
	(49, 40114, 14, '2023-11-10', '2023-11-13', '2023-11-12'),
	(50, 40115, 15, '2023-09-05', '2023-09-08', '2023-09-08');

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
-- Populando emprestimo
INSERT INTO emprestimo (cod_exemplar, cod_matricula, dt_emprestimo, dt_devolucao)
	VALUES
	(1, 40101, '2022-12-17', '2022-12-24'),
	(2, 40102, '2021-12-01', '2021-12-08'),
	(3, 40103, '2021-11-08', '2021-11-15'),
	(4, 40104, '2022-10-12', '2022-10-19'),
	(5, 40105, '2022-03-09', '2022-03-16'),
	(6, 40101, '2021-09-25', '2021-10-02'),
	(7, 40102, '2022-08-17', '2022-08-24'),
	(8, 40113, '2021-07-04', '2021-07-11'),
	(9, 40114, '2022-01-22', '2022-01-29'),
	(10, 40115, '2022-06-14', '2022-06-21'),
	(11, 40111, '2021-05-31', '2021-06-07'),
	(12, 40112, '2022-04-04', '2022-04-11'),
	(13, 40113, '2022-02-19', '2022-02-26'),
	(14, 40114, '2021-11-13', '2021-11-20'),
	(15, 40115, '2021-09-08', '2021-09-15'),
	(16, 40111, '2022-07-16', '2022-07-23'),
	(17, 40122, '2022-01-01', '2022-01-08'),
	(18, 40123, '2022-03-26', '2022-04-02'),
	(19, 40124, '2022-05-21', '2022-05-28'),
	(20, 40125, '2021-08-12', '2021-08-19'),
	(21, 40121, '2022-06-20', '2022-06-27'),
	(22, 40122, '2021-11-03', '2021-11-10'),
	(23, 40123, '2021-10-07', '2021-10-14'),
	(24, 40124, '2022-11-12', '2022-11-19'),
	(25, 40125, '2022-04-09', '2022-04-16'),
	(26, 40131, '2021-10-24', '2021-10-31'),
	(27, 40131, '2022-09-17', '2022-09-24'),
	(28, 40134, '2021-08-04', '2021-08-11'),
	(29, 40134, '2022-02-12', '2022-02-19'),
	(30, 40131, '2022-06-04', '2022-06-11'),
	(31, 40142, '2023-02-17', '2023-02-24'),
	(32, 40145, '2023-04-07', '2023-04-14'),
	(33, 40141, '2023-06-22', '2023-06-29'),
	(34, 40143, '2023-08-14', '2023-08-21'),
	(35, 40145, '2023-10-12', '2023-10-19'),
	(36, 40141, '2023-12-20', '2023-12-27'),
	(37, 40142, '2022-12-01', '2022-12-08'),
	(38, 40143, '2022-11-08', '2022-11-15'),
	(39, 40144, '2023-10-12', '2023-10-19'),
	(40, 40155, '2023-03-09', '2023-03-16'),
	(41, 40152, '2023-09-25', '2023-10-02'),
	(42, 40153, '2022-08-17', '2022-08-24'),
	(43, 40154, '2023-01-03', '2023-01-10'),
	(44, 40155, '2023-05-22', '2023-05-29'),
	(45, 40151, '2022-06-14', '2022-06-21'),
	(46, 40152, '2022-03-31', '2022-04-07'),
	(47, 40153, '2023-03-17', '2023-03-24'),
	(48, 40154, '2021-12-24', '2021-12-31'),
	(49, 40155, '2023-11-12', '2023-11-19'),
	(50, 40151, '2023-09-08', '2023-09-15');

UPDATE emprestimo 
	SET dt_prevista_devolucao = dt_emprestimo + 14
