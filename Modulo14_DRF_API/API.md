# API


- Listar horários: `GET /horarios/`
["7:00", "19:30"]


- Listar agendamentos: `GET /agendamentos/`
[
  {
    "nome": "Sergio",
    "telefone": "1313123131",
    "email": "sergio@email.com",
  }
]


- Detalhar agendamento: `GET /agendamentos/<id>/`


- Criar agendamento: `POST /agendamentos/`


- Excluir agendamento: `DELETE /agendamentos/<id>/`


- Editar agendamento: `PUT/PATCH /agendamentos/<id>/`