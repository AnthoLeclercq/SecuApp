import { Box, CircularProgress, Typography } from '@mui/material';
import { RootState } from 'app/rootReducer';
import React, { useEffect } from 'react';
import { useSelector } from 'react-redux';

const Loader: React.FC = () => {
  const {isLoading} = useSelector((state: RootState) => state.loader); 

  
  useEffect(() => {
  },[isLoading]);

  return (
    <>
    {isLoading && (
      <Box
      sx={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        background: 'rgba(255, 255, 255, 0.8)',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 9999,
      }}
      >
        <Typography variant="body2" mt={1}>
          Chargement en cours...
        </Typography>
        <CircularProgress />
        
      </Box>
    )}
    </>
    
  );
};

export default Loader;