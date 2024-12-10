import { Avatar, Box, Button, Checkbox, Container, Divider, FormControlLabel, Grid, Link, TextField } from '@mui/material';
import Typography from '@mui/material/Typography';
import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { registerUser, useCurrentUser } from './authApi';

const RegisterPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const currentUser = useCurrentUser();
  const [errorMdp, setErrorMdp] = useState<string | null>(null)
  const [isAdmin, setIsAdmin] = useState(false);

  const handleCheckboxChange = (event) => {
    setIsAdmin(event.target.checked);
  };


  function sucessRegister(){
    navigate("/manageuser");
  }

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const roleValue = data.get('role') === 'on' ? 'admin' : 'user';
    if(data.get('password') !== data.get('confirmPassword')){
      setErrorMdp("Le mot de passe et le mot de passe de confirmation ne sont pas identique")
    }else{
      data.set('role', roleValue);
      dispatch<any>(registerUser(currentUser!.token,data, sucessRegister))
      setErrorMdp(null)
    }
  };

  useEffect(() => {
  }, []);

  return (
    <>
    <Container>
        <Grid item mb={2} xs={12}>
          <Typography variant="h4" letterSpacing={5} align="left" my={2} gutterBottom >
            Gestion des Utilisateurs
          </Typography>
          <Divider sx={{ backgroundColor: 'blue' }} />
        </Grid>
      </Container>
    <Container component="main" maxWidth="xs">
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          </Avatar>
          <Typography component="h1" variant="h5">
            Création utilisateur
          </Typography>

          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 1 }}>
            <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email"
                name="email"
                autoComplete="email"
                autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="firstname"
              label="Prénom"
              name="firstname"
              autoComplete="firstname"
              autoFocus

            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="lastname"
              label="Nom"
              name="lastname"
              autoComplete="lastname"
              autoFocus

            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Mot de passe"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="confirmPassword"
              label="Confirmation du mot de passe"
              type="password"
              id="confirmPassword"
              autoComplete="current-password"
              error={errorMdp !== null}
              helperText={errorMdp || ""}
            />
            <FormControlLabel
              name="role"
              id="role"
              control={<Checkbox checked={isAdmin} onChange={handleCheckboxChange} />}
              label="Administrateur"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Créer
            </Button>
          </Box>
        </Box>
      </Container>
    </>
      
  );
};

export default RegisterPage;
