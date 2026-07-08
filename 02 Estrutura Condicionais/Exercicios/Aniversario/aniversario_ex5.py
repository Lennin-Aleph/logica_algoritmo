valor_imprestimo = float(input("Qual valor do emprestimo? "))
qnt_parcelas = int(input("Quantas parcelas? "))
juros = valor_imprestimo * 0.20
total_devido = valor_imprestimo + juros
vlr_parcela = total_devido / qnt_parcelas


print(f" Valor final do emprestimo de R$ {total_devido:.2f} \n Parcelado em {qnt_parcelas} x R$ {vlr_parcela}")