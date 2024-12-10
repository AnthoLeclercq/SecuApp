import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { logout } from './Auth/authApi';
import { setLoader } from './loader/loaderAction';

export const fetchApi = async ({
  method,
  endpoint,
  token,
  data,
  funcSuccess,
  dispatch,
  showLoader = true,
}: {
  method: string;
  endpoint: string;
  token?: string;
  data?: any;
  funcSuccess: (responseData: any) => void;
  dispatch: any,
  showLoader?: boolean;
}) => {
  const url = process.env.REACT_APP_API_URL + endpoint;
  const headers = {
    //'Access-Control-Allow-Origin': process.env.REACT_APP_API_URL,
  };

  if (token) {
    headers['Authorization'] = token;
  }

  try {
    if (showLoader) {
      dispatch(setLoader(true));
    }

    let options: any = {
      method,
      headers,
    };

    if (method === 'POST' || method === 'PUT') {
      if (data instanceof FormData) {
        options.body = data;
      } else {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(data);
      }
    }

    const response = await fetch(url, options);

    if (response.ok) {
      const responseData = await response.json();
      funcSuccess(responseData);
    } else {
      if (response.status === 401) {
        dispatch(logout());
      }else{
        throw response;
      }
      
    }
  } catch (error) {
    if(process.env.REACT_APP_ENV === "developpement"){
      console.error(error)
    }

    if (error instanceof Response) {
      const responseError = await error.json();
      if(responseError.displayError){
        toast.error(responseError.displayError);
      }else{
        toast.error('Une erreur s\'est produite. Veuillez réessayer.');
      }
    }
    else{
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }  
  }
   finally {
    if (showLoader) {
      dispatch(setLoader(false));
    }
  }
};
