import { Grid } from '@mui/material';
import Typography from '@mui/material/Typography';
import React, { FC } from 'react';
import logo from "../images/logo192.png";


interface HeaderProps {
  libelleTxt: string;
}

const HeaderPage: FC<HeaderProps> = ({libelleTxt}) => {

  return (
    <Grid container alignItems="center" sx={{backgroundColor: "black"}}>
      <Grid item mb={2} xs={1} >
        <img src={logo} alt="Logo" style={{height: "70px"}}/>
      </Grid>
      <Grid item xs={10} >
        <Typography variant="h3" sx={{fontFamily: "Roboto", color:"white"}} letterSpacing={4} align="center" my={2} gutterBottom >
          {libelleTxt}
        </Typography>
      </Grid>
      <Grid item mb={2} xs={1} >
        <img src={logo} alt="Logo" style={{height: "70px"}}/>
      </Grid>
    </Grid>
  );
}

export default HeaderPage;