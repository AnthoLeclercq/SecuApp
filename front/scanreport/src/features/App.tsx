import { CssBaseline, Grid, Container, Paper, ThemeProvider, createTheme } from "@mui/material"
import Header from "page/Header"
import React from "react"
import { Routes, Route, Navigate } from "react-router-dom"
import { useCurrentUser, useLogged } from './Auth/authApi';
import LoginPage from "./Auth/LoginPage"
import AccueilPage from "./Accueil/AccueilPage";
import { colors } from "./colors";
import ApiPage from "./Api/ApiPage";

function App() {

    const logged = useLogged();
    const user = useCurrentUser();
    const theme = createTheme({
        components: {
          MuiCssBaseline: {
            styleOverrides: (themeParam) => ({
              body: {backgroundColor : colors.vert_fond},
            }),
          },
        },
        palette: {
            secondary: {
                main: '#d32f2f'
            },
            primary: {
                main: colors.primary
            }
          },
      });

    return (
        <div className="App">
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <Header />
                <Container sx={{minHeight: "100vh"}} maxWidth="lg">
                <Paper square={true} sx={{minHeight: "100vh", pt:1}}>
                    <Grid item xs>
                        <main>
                            <Routes>
                                <Route path="/" element={<AccueilPage />} />
                                <Route path="/api" element={<ApiPage />} />
                                <Route path="/*" element={<Navigate to="/" />} />
                            </Routes>
                        </main>
                    </Grid>
                </Paper>
                </Container>
            </ThemeProvider>

        </div>
    )
}

export default App