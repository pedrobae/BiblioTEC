-- Livros atrasados e quem os emprestou
SELECT mat.nome_matricula, liv.titulo, emp.dt_devolucao - emp.dt_prevista_devolucao AS "Dias Atrasados"
    FROM emprestimo emp JOIN matricula mat
        ON (emp.cod_matricula = mat.cod_matricula)
                        JOIN exemplar ex
        ON (emp.cod_exemplar = ex.cod_exemplar)
                        JOIN livro liv
        ON (ex.ISBN = liv.ISBN)
    WHERE emp.dt_devolucao > emp.dt_prevista_devolucao
    ORDER BY "Dias Atrasados" DESC;

-- Lista de reserva de um exemplar e seus e-mail
SELECT mat.nome_matricula, mat.email_matricula, res.dt_prevista_emprestimo, liv.titulo
    FROM reserva res JOIN matricula mat
        ON (res.cod_matricula = mat.cod_matricula)
                     JOIN exemplar ex
        ON (res.cod_exemplar = ex.cod_exemplar)
                     JOIN livro liv
        ON (ex.ISBN = liv.ISBN)
    WHERE res.dt_emprestimo IS NULL AND res.cod_exemplar = 'INSERIR CODIGO DO EXEMPLAR'
    ORDER BY dt_prevista_emprestimo;

-- Consulta de livros emprestados
SELECT liv.ISBN, liv.titulo, exe.cod_exemplar, mat.cod_matricula, mat.nome, emp.dt_emprestimo, emp.dt_prevista_devolucao
    FROM livro liv JOIN exemplar exe
        ON (liv.ISBN = exe.ISBN)
                   JOIN emprestimo emp
        ON (exe.cod_exemplar = emp.cod_exemplar)
                   JOIN matricula mat
        ON (mat.cod_matricula = emp.cod_matricula)
    WHERE emp.dt_devolucao IS NULL;
                    
-- Consultar histórico de aluno/ professor / funcionário
SELECT mat.nome_matricula, mat.cod_tipo_matricula, ex.cod_exemplar, liv.titulo, emp.dt_emprestimo, emp.dt_devolucao
    FROM matricula mat JOIN emprestimo emp
        ON (emp.cod_matricula = mat.cod_matricula)
                       JOIN exemplar ex
        ON (ex.cod_exemplar= emp.cod_exemplar)
                       JOIN livro liv
        ON (ex.ISBN = liv.ISBN )
    WHERE emp.cod_matricula ='INSERIR CODIGO DE MATRICULA'
    ORDER BY dt_emprestimo DESC
