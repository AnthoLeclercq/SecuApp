import IconButton from '@mui/material/IconButton';
import { AccountCircle, ExitToApp } from '@material-ui/icons';
import { AppBar, Box, Button, Toolbar } from '@mui/material';
import Typography from '@mui/material/Typography';
import { useCurrentUser, logout } from 'features/Auth/authApi';
import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { colors } from 'features/colors';

const Header: React.FC = () => {
  const user = useCurrentUser();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar sx={{backgroundColor: colors.vert_pomme}} position="static">
        <Toolbar>
        <Box textAlign="left" style={{ margin: 5, marginRight: 20 }}>
            <Typography variant='h4' style={{fontSize: '200%'}}>Scan-Report</Typography>
          </Box>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            <Button
              onClick={e => navigate("/")}
              sx={{ mx: 1, color: 'white', display: 'block' }}
            >
              {"Analyse"}
            </Button>
            <Button
              onClick={e => navigate("/api")}
              sx={{ mx: 1, color: 'white', display: 'block' }}
            >
              {"API"}
            </Button>
          </Box>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default Header;