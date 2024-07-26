import { ManifestForm } from 'src/components/Manifest';
import { HtSpinner } from 'src/components/UI';
import { useTitle } from 'src/hooks';
import { useReadOnly } from 'src/hooks/manifest';
import React from 'react';
import { useParams } from 'react-router-dom';
import { useGetManifestQuery } from 'src/store';

export function ManifestDetails() {
  const { mtn, action, siteId } = useParams();
  useTitle(`${mtn}`);
  const { data, error, isLoading } = useGetManifestQuery(mtn!, { skip: !mtn });
  useReadOnly(true);

  const readOnly = action !== 'edit';

  if (error) {
    return (
      <div className="text-danger">
        <h2>Something went wrong</h2>
        <p>{error.message}</p>
      </div>
    );
  }

  return isLoading ? (
    <HtSpinner center />
  ) : data ? (
    <ManifestForm manifestData={data} readOnly={readOnly} manifestingSiteID={siteId} mtn={mtn} />
  ) : (
    <div className="text-danger">
      <h2>Something went wrong</h2>
    </div>
  );
}
