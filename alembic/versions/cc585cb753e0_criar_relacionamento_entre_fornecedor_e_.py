"""Criar relacionamento entre fornecedor e conta a pagar

Revision ID: cc585cb753e0
Revises: d28ecb421854
Create Date: 2024-05-29 13:52:22.420481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc585cb753e0'
down_revision: Union[str, None] = 'd28ecb421854'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contas_a_pagar_e_receber', sa.Column('fornecedor_cliente_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contas_a_pagar_e_receber', 'fornecedor_cliente', ['fornecedor_cliente_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contas_a_pagar_e_receber', type_='foreignkey')
    op.drop_column('contas_a_pagar_e_receber', 'fornecedor_cliente_id')
    # ### end Alembic commands ###
