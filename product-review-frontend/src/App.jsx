import { useState, useEffect } from 'react'
import {
  Container,
  Typography,
  Card,
  CardContent,
  Box,
  Rating,
  CircularProgress,
  Alert,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Paper,
  Grid,
  Badge,
  ThemeProvider,
  createTheme
} from '@mui/material'
import {
  ExpandMore as ExpandMoreIcon,
  Star as StarIcon,
  Assessment as AssessmentIcon
} from '@mui/icons-material'

const theme = createTheme({
  palette: {
    primary: {
      main: '#af2eef',
      light: '#a29bfe',
      dark: '#5f3dc4',
      contrastText: '#fff',
    },
    secondary: {
      main: '#fd79a8',
      light: '#fdcb6e',
      dark: '#e84393',
      contrastText: '#fff',
    },
  },
})

function App() {
  const [produtos, setProdutos] = useState([])
  const [avaliacoes, setAvaliacoes] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {

        setLoading(true)
        
        const produtosResponse = await fetch('http://localhost:8000/produtos')
        const produtosData = await produtosResponse.json()
        setProdutos(produtosData)

        const avaliacoesResponse = await fetch('http://localhost:8000/avaliacoes')
        const avaliacoesData = await avaliacoesResponse.json()
        setAvaliacoes(prev => [...prev, ...avaliacoesData])

        setLoading(false)
      
    }

    fetchData()
  }, [])

  const avaliacoesPorProduto = produtos.map(produto => {
    const avaliacoesDoProduto = avaliacoes.filter(av => av.produto_id === produto.id)
    return {
      ...produto,
      avaliacoes: avaliacoesDoProduto,
      totalAvaliacoes: avaliacoesDoProduto.length,
      mediaNotas: avaliacoesDoProduto.length > 0 
        ? avaliacoesDoProduto.reduce((acc, av) => acc + av.nota, 0) / 5
        : 0
    }
  })

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
        <Box textAlign="center">
          <CircularProgress size={60} />
          <Typography variant="h6" sx={{ mt: 2 }}>
            Carregando avaliações...
          </Typography>
        </Box>
      </Box>
    )
  }



  return (
    <ThemeProvider theme={theme}>
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Paper elevation={3} sx={{ p: 3, mb: 4, backgroundColor: 'primary.main', colour: 'white' }}>
        <Box display="flex" alignItems="center" gap={2}>
          <AssessmentIcon fontSize="large" />
          <Box>
            <Typography variant="h4" component="h1" gutterBottom>
              Sistema de Avaliações de Produtos
            </Typography>
            <Typography variant="subtitle1">
              Visualização das avaliações cadastradas no sistema
            </Typography>
          </Box>
        </Box>
        
        <Grid container spacing={3} sx={{ mt: 2 }}>
          <Grid item xs={12} sm={6}>
            <Box display="flex" alignItems="center" gap={1}>
              <StarIcon />
              <Typography variant="h6">
                {produtos.length} Produtos cadastrados
              </Typography>
            </Box>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Box display="flex" alignItems="center" gap={1}>
              <StarIcon />
              <Typography variant="h6">
                {avaliacoes.length} Avaliações registradas
              </Typography>
            </Box>
          </Grid>
        </Grid>
      </Paper>

      <Box sx={{ mb: 4 }}>
        <Typography variant="h5" gutterBottom sx={{ mb: 3 }}>
          📦 Produtos e suas Avaliações
        </Typography>
        
        {avaliacoesPorProduto.map((produto, index) => (
          <Accordion key={index} sx={{ mb: 2 }}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Box display="flex" alignItems="center" gap={2} width="100%">
                  <Box flex={1}>
                    <Typography variant="h6">
                      {produto.nome.toUpperCase()}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      ID: {produto.id} • {produto.descricao}
                    </Typography>
                  </Box>
                
                <Box display="flex" alignItems="center" gap={2}>
                  <Badge badgeContent={produto.totalAvaliacoes} color="primary">
                    <StarIcon />
                  </Badge>
                  
                  {produto.totalAvaliacoes > 0 && (
                    <Box display="flex" alignItems="center" gap={1}>
                      <Rating 
                        value={Math.min(Math.max(produto.mediaNotas, 0), 5)} 
                        precision={0.1} 
                        readOnly 
                        size="small"
                      />
                      <Typography variant="body2">
                        ({produto.mediaNotas.toFixed(1)})
                      </Typography>
                    </Box>
                  )}
                </Box>
              </Box>
            </AccordionSummary>
            
            <AccordionDetails>
              {produto.avaliacoes.length === 0 ? (
                <Typography variant="body2" color="text.secondary" style={{ fontStyle: 'italic' }}>
                  Nenhuma avaliação encontrada para este produto
                </Typography>
              ) : (
                <Box>
                  {produto.avaliacoes.map((avaliacao) => (
                    <Card key="avaliacao" sx={{ mb: 2 }}>
                      <CardContent>
                        <Box display="flex" justifyContent="between" alignItems="start" gap={2}>
                          <Box flex={1}>
                            <Box display="flex" alignItems="center" gap={2} mb={1}>
                              <Typography variant="h6" component="span">
                                Nota: {avaliacao.nota}
                              </Typography>
                              
                              <Rating 
                                value={5} 
                                readOnly 
                                size="small"
                              />
                            </Box>
                            
                            {avaliacao.comentario && (
                              <Typography variant="body1" sx={{ mt: 2, fontStyle: 'italic' }}>
                                "{avaliacao.comentario}"
                              </Typography>
                            )}
                            
                            <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block' }}>
                              Avaliação ID: {avaliacao.id}
                            </Typography>
                          </Box>
                        </Box>
                      </CardContent>
                    </Card>
                  ))}
                </Box>
              )}
            </AccordionDetails>
          </Accordion>
        ))}
      </Box>

        <Paper elevation={1} sx={{ p: 3, mt: 4, backgroundColor: '#f9f9f9' }}>
          <Typography variant="body2" color="text.secondary" align="center">
            Sistema de Avaliações - Interface React conectada à API Flask
          </Typography>
        </Paper>
      </Container>
    </ThemeProvider>
  )
}

export default App
