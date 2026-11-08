describe('Acesso ao Planner', () => {
  it('Deve carregar a página inicial com sucesso', () => {
    cy.visit('https://planner.guttester.io/')
    cy.url().should('include', 'planner.guttester.io')
  })
})