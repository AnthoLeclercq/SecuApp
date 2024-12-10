import { Avatar, Box, Button, Container, TextField } from '@mui/material';
import Typography from '@mui/material/Typography';
import React from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { loginUser } from './authApi';

const LoginPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();


  function sucessLogin(){
    navigate("/");
  }

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    dispatch<any>(loginUser(data,sucessLogin))
  };

  return (
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
            {/*<LockOutlinedIcon />*/}
          </Avatar>
          <Typography component="h1" variant="h5">
            connexion
          </Typography>

          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="username"
              label="Email"
              name="email"
              autoComplete="email"
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
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Connexion
            </Button>
          </Box>
        </Box>
      </Container>
  );
};

export default LoginPage;