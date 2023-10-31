-- Livros atrasados e quem os emprestou
SELECT titulo, nome_matricula, data_prevista_emprestimo
    FROM emprestimo emp JOIN matricula mat
        ON (emp.cod_matricula, mat.cod_matricula)
                        JOIN exemplar ex
        ON (emp.cod_exemplar, ex.cod_exemplar)
                        JOIN livro liv
        ON (ex.ISBN, liv.ISBN)
            WHERE dt_devolucao > dt_prevista_devolucao;


-- Lista de reserva de um exemplar e seus e-mail
