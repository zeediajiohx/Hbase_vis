import happybase
connection = happybase.Connection('192.168.56.101')

# connection.create_table(
#     'populations',
#     {
#
#         'popu': dict(),
#         'rank': dict(),
#         'cont': dict(),
#
#
#     }
# )
print(connection.tables())
