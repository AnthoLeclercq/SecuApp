import { Box, Container, Divider, Grid, Tabs, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useCurrentUser } from "features/Auth/authApi";
import { useDispatch } from "react-redux";
import { colors } from "features/colors";
import logo from "../../images/logo192.png";
import Tab from '@mui/material/Tab';
import ParametrageBloc from "./Bloc/ParametrageBloc";
import GenerationBloc from "./Bloc/GenerationBloc";
import HistoriqueBloc from "./Bloc/HistoriqueBloc";
import HeaderPage from "page/HeaderPage";


const AccueilPage = () => {
  const currentUser = useCurrentUser();
  const dispatch = useDispatch();

  const [tableValue, setTableValue] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTableValue(newValue);
  };


  useEffect(() => {
    //
  }, []);

  return (
    <Container>
      <Grid container>
        <HeaderPage libelleTxt="Analyse et rapports"/>
      </Grid>
      <Box sx={{ width: '100%' }}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <Tabs value={tableValue} onChange={handleChange} aria-label="table rapport">
            <Tab label="Paramétrage" />
            <Tab label="Généreration de rapports" />
            <Tab label="Rapports" />
          </Tabs>
        </Box>
        <Box>
          {tableValue === 0 && (
            <ParametrageBloc />
          )}
          {tableValue === 1 && (
            <GenerationBloc />
          )}
          {tableValue === 2 && (
            <HistoriqueBloc />
          )}
        </Box>
      </Box>
    </Container>
  );
}

export default AccueilPage;
