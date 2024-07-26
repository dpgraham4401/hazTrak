import React, { ReactElement, Suspense } from 'react';
import { Container } from 'react-bootstrap';
import { Provider } from 'react-redux';
import { RouterProvider } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { ErrorBoundary } from 'src/components/Error';
import { Notifications } from 'src/components/Notifications/Notifications';
import { HtSpinner } from 'src/components/UI';
import { router } from 'src/routes';
import './App.scss';
import { rootStore } from 'src/store';

// // initiate the mock service worker if deployed in TEST environment
// // intercepts API calls and returns fake/test responses
// if (process.env.NEXT_PUBLIC_HT_ENV && process.env.NEXT_PUBLIC_HT_ENV.toUpperCase() === 'TEST') {
//   const { worker } = require('./test-utils/mock/browser');
//   worker.start();
// }

const GlobalSpinner = () => (
  <Container fluid className="d-flex justify-content-center align-items-center vh-100">
    <HtSpinner size="6x" className="my-auto" />
  </Container>
);

function App(): ReactElement {
  return (
    <React.StrictMode>
      <Provider store={rootStore}>
        <ErrorBoundary>
          <ToastContainer
            position="bottom-right"
            autoClose={5000}
            hideProgressBar={false}
            newestOnTop
            closeOnClick
            pauseOnHover
            limit={3}
          />
          <Notifications />
          <Suspense fallback={<GlobalSpinner />}>
            <RouterProvider router={router} />
          </Suspense>
        </ErrorBoundary>
      </Provider>
    </React.StrictMode>
  );
}

export default App;
