# Copyright 2015 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# Include this gypi to include all 'gpu' files
# The parent gyp/gypi file must define
#       'skia_src_path'     e.g. skia/trunk/src
#       'skia_include_path' e.g. skia/trunk/include
#
# The skia build defines these in common_variables.gypi
#
{
  'variables': {
    'skgpu_sources': [
      '<(skia_include_path)/gpu/GrBlend.h',
      '<(skia_include_path)/gpu/GrBuffer.h',
      '<(skia_include_path)/gpu/GrBufferAccess.h',
      '<(skia_include_path)/gpu/GrCaps.h',
      '<(skia_include_path)/gpu/GrClip.h',
      '<(skia_include_path)/gpu/GrColor.h',
      '<(skia_include_path)/gpu/GrColorSpaceXform.h',
      '<(skia_include_path)/gpu/GrConfig.h',
      '<(skia_include_path)/gpu/GrContextOptions.h',
      '<(skia_include_path)/gpu/GrContext.h',
      '<(skia_include_path)/gpu/GrCoordTransform.h',
      '<(skia_include_path)/gpu/GrDrawContext.h',
      '<(skia_include_path)/gpu/GrFragmentProcessor.h',
      '<(skia_include_path)/gpu/GrGpuResource.h',
      '<(skia_include_path)/gpu/GrInvariantOutput.h',
      '<(skia_include_path)/gpu/GrPaint.h',
      '<(skia_include_path)/gpu/GrProcessor.h',
      '<(skia_include_path)/gpu/GrProcessorUnitTest.h',
      '<(skia_include_path)/gpu/GrProgramElement.h',
      '<(skia_include_path)/gpu/GrGpuResourceRef.h',
      '<(skia_include_path)/gpu/GrRenderTarget.h',
      '<(skia_include_path)/gpu/GrResourceKey.h',
      '<(skia_include_path)/gpu/GrShaderVar.h',
      '<(skia_include_path)/gpu/GrSurface.h',
      '<(skia_include_path)/gpu/GrTexture.h',
      '<(skia_include_path)/gpu/GrTextureParams.h',
      '<(skia_include_path)/gpu/GrTextureProvider.h',
      '<(skia_include_path)/gpu/GrTextureAccess.h',
      '<(skia_include_path)/gpu/GrTestUtils.h',
      '<(skia_include_path)/gpu/GrTypes.h',
      '<(skia_include_path)/gpu/GrTypesPriv.h',
      '<(skia_include_path)/gpu/GrXferProcessor.h',

      '<(skia_include_path)/gpu/effects/GrConstColorProcessor.h',
      '<(skia_include_path)/gpu/effects/GrCoverageSetOpXP.h',
      '<(skia_include_path)/gpu/effects/GrCustomXfermode.h',
      '<(skia_include_path)/gpu/effects/GrPorterDuffXferProcessor.h',
      '<(skia_include_path)/gpu/effects/GrXfermodeFragmentProcessor.h',

      '<(skia_include_path)/gpu/gl/GrGLAssembleInterface.h',
      '<(skia_include_path)/gpu/gl/GrGLConfig.h',
      '<(skia_include_path)/gpu/gl/GrGLExtensions.h',
      '<(skia_include_path)/gpu/gl/GrGLFunctions.h',
      '<(skia_include_path)/gpu/gl/GrGLInterface.h',
      '<(skia_include_path)/gpu/gl/GrGLSLPrettyPrint.h',
      '<(skia_include_path)/gpu/gl/GrGLTypes.h',

      # Private includes
      '<(skia_include_path)/private/GrAuditTrail.h',
      '<(skia_include_path)/private/GrInstancedPipelineInfo.h',
      '<(skia_include_path)/private/GrSingleOwner.h',
      '<(skia_include_path)/private/GrRenderTargetProxy.h',
      '<(skia_include_path)/private/GrSurfaceProxy.h',
      '<(skia_include_path)/private/GrTextureProxy.h',
      '<(skia_include_path)/private/GrTextureStripAtlas.h',

      '<(skia_src_path)/gpu/GrAppliedClip.h',
      '<(skia_src_path)/gpu/GrAuditTrail.cpp',
      '<(skia_src_path)/gpu/GrAutoLocaleSetter.h',
      '<(skia_src_path)/gpu/GrAllocator.h',
      '<(skia_src_path)/gpu/GrBatchAtlas.cpp',
      '<(skia_src_path)/gpu/GrBatchAtlas.h',
      '<(skia_src_path)/gpu/GrBatchFlushState.cpp',
      '<(skia_src_path)/gpu/GrBatchFlushState.h',
      '<(skia_src_path)/gpu/GrBatchTest.cpp',
      '<(skia_src_path)/gpu/GrBatchTest.h',
      '<(skia_src_path)/gpu/GrBlend.cpp',
      '<(skia_src_path)/gpu/GrBlurUtils.cpp',
      '<(skia_src_path)/gpu/GrBlurUtils.h',
      '<(skia_src_path)/gpu/GrBuffer.cpp',
      '<(skia_src_path)/gpu/GrBufferAllocPool.cpp',
      '<(skia_src_path)/gpu/GrBufferAllocPool.h',
      '<(skia_src_path)/gpu/GrCaps.cpp',
      '<(skia_src_path)/gpu/GrClipStackClip.h',
      '<(skia_src_path)/gpu/GrClipStackClip.cpp',
      '<(skia_src_path)/gpu/GrColorSpaceXform.cpp',
      '<(skia_src_path)/gpu/GrContext.cpp',
      '<(skia_src_path)/gpu/GrContextPriv.h',
      '<(skia_src_path)/gpu/GrCoordTransform.cpp',
      '<(skia_src_path)/gpu/GrDefaultGeoProcFactory.cpp',
      '<(skia_src_path)/gpu/GrDefaultGeoProcFactory.h',
      '<(skia_src_path)/gpu/GrDrawContext.cpp',
      '<(skia_src_path)/gpu/GrDrawContextPriv.h',
      '<(skia_src_path)/gpu/GrPathRenderingDrawContext.cpp',
      '<(skia_src_path)/gpu/GrPathRenderingDrawContext.h',
      '<(skia_src_path)/gpu/GrDrawingManager.cpp',
      '<(skia_src_path)/gpu/GrDrawingManager.h',
      '<(skia_src_path)/gpu/GrDrawTarget.cpp',
      '<(skia_src_path)/gpu/GrDrawTarget.h',
      '<(skia_src_path)/gpu/GrFixedClip.cpp',
      '<(skia_src_path)/gpu/GrFixedClip.h',
      '<(skia_src_path)/gpu/GrFragmentProcessor.cpp',
      '<(skia_src_path)/gpu/GrGeometryProcessor.h',
      '<(skia_src_path)/gpu/GrGlyph.h',
      '<(skia_src_path)/gpu/GrGpu.cpp',
      '<(skia_src_path)/gpu/GrGpu.h',
      '<(skia_src_path)/gpu/GrGpuResourceCacheAccess.h',
      '<(skia_src_path)/gpu/GrGpuCommandBuffer.cpp',
      '<(skia_src_path)/gpu/GrGpuCommandBuffer.h',
      '<(skia_src_path)/gpu/GrGpuResourcePriv.h',
      '<(skia_src_path)/gpu/GrGpuResource.cpp',
      '<(skia_src_path)/gpu/GrGpuFactory.cpp',
      '<(skia_src_path)/gpu/GrGpuFactory.h',
      '<(skia_src_path)/gpu/GrImageIDTextureAdjuster.cpp',
      '<(skia_src_path)/gpu/GrImageIDTextureAdjuster.h',
      '<(skia_src_path)/gpu/GrInvariantOutput.cpp',
      '<(skia_src_path)/gpu/GrMemoryPool.cpp',
      '<(skia_src_path)/gpu/GrMemoryPool.h',
      '<(skia_src_path)/gpu/GrMesh.h',
      '<(skia_src_path)/gpu/GrNonAtomicRef.h',
      '<(skia_src_path)/gpu/GrOvalRenderer.cpp',
      '<(skia_src_path)/gpu/GrOvalRenderer.h',
      '<(skia_src_path)/gpu/GrPaint.cpp',
      '<(skia_src_path)/gpu/GrPath.cpp',
      '<(skia_src_path)/gpu/GrPath.h',
      '<(skia_src_path)/gpu/GrPathProcessor.cpp',
      '<(skia_src_path)/gpu/GrPathProcessor.h',
      '<(skia_src_path)/gpu/GrPathRange.cpp',
      '<(skia_src_path)/gpu/GrPathRange.h',
      '<(skia_src_path)/gpu/GrPathRendererChain.cpp',
      '<(skia_src_path)/gpu/GrPathRendererChain.h',
      '<(skia_src_path)/gpu/GrPathRenderer.cpp',
      '<(skia_src_path)/gpu/GrPathRenderer.h',
      '<(skia_src_path)/gpu/GrPathRendering.cpp',
      '<(skia_src_path)/gpu/GrPathRendering.h',
      '<(skia_src_path)/gpu/GrPathUtils.cpp',
      '<(skia_src_path)/gpu/GrPathUtils.h',
      '<(skia_src_path)/gpu/GrPendingProgramElement.h',
      '<(skia_src_path)/gpu/GrPipeline.cpp',
      '<(skia_src_path)/gpu/GrPipeline.h',
      '<(skia_src_path)/gpu/GrPipelineBuilder.cpp',
      '<(skia_src_path)/gpu/GrPipelineBuilder.h',
      '<(skia_src_path)/gpu/GrPrimitiveProcessor.cpp',
      '<(skia_src_path)/gpu/GrPrimitiveProcessor.h',
      '<(skia_src_path)/gpu/GrProgramDesc.cpp',
      '<(skia_src_path)/gpu/GrProgramDesc.h',
      '<(skia_src_path)/gpu/GrProgramElement.cpp',
      '<(skia_src_path)/gpu/GrProcessor.cpp',
      '<(skia_src_path)/gpu/GrProcessorUnitTest.cpp',
      '<(skia_src_path)/gpu/GrProcOptInfo.cpp',
      '<(skia_src_path)/gpu/GrProcOptInfo.h',
      '<(skia_src_path)/gpu/GrGpuResourceRef.cpp',
      '<(skia_src_path)/gpu/GrQuad.h',
      '<(skia_src_path)/gpu/GrRect.h',
      '<(skia_src_path)/gpu/GrRectanizer.h',
      '<(skia_src_path)/gpu/GrRectanizer_pow2.cpp',
      '<(skia_src_path)/gpu/GrRectanizer_pow2.h',
      '<(skia_src_path)/gpu/GrRectanizer_skyline.cpp',
      '<(skia_src_path)/gpu/GrRectanizer_skyline.h',
      '<(skia_src_path)/gpu/GrRenderTarget.cpp',
      '<(skia_src_path)/gpu/GrRenderTargetPriv.h',
      '<(skia_src_path)/gpu/GrRenderTargetProxy.cpp',
      '<(skia_src_path)/gpu/GrReducedClip.cpp',
      '<(skia_src_path)/gpu/GrReducedClip.h',
      '<(skia_src_path)/gpu/GrResourceCache.cpp',
      '<(skia_src_path)/gpu/GrResourceCache.h',
      '<(skia_src_path)/gpu/GrResourceHandle.h',
      '<(skia_src_path)/gpu/GrResourceProvider.cpp',
      '<(skia_src_path)/gpu/GrResourceProvider.h',
      '<(skia_src_path)/gpu/GrScissorState.h',
      '<(skia_src_path)/gpu/GrShape.cpp',
      '<(skia_src_path)/gpu/GrShape.h',
      '<(skia_src_path)/gpu/GrStencilAttachment.cpp',
      '<(skia_src_path)/gpu/GrStencilAttachment.h',
      '<(skia_src_path)/gpu/GrStencilSettings.cpp',
      '<(skia_src_path)/gpu/GrStencilSettings.h',
      '<(skia_src_path)/gpu/GrStyle.cpp',
      '<(skia_src_path)/gpu/GrStyle.h',
      '<(skia_src_path)/gpu/GrTessellator.cpp',
      '<(skia_src_path)/gpu/GrTessellator.h',
      '<(skia_src_path)/gpu/GrTraceMarker.cpp',
      '<(skia_src_path)/gpu/GrTraceMarker.h',
      '<(skia_src_path)/gpu/GrTracing.h',
      '<(skia_src_path)/gpu/GrTestUtils.cpp',
      '<(skia_src_path)/gpu/GrSWMaskHelper.cpp',
      '<(skia_src_path)/gpu/GrSWMaskHelper.h',
      '<(skia_src_path)/gpu/GrSoftwarePathRenderer.cpp',
      '<(skia_src_path)/gpu/GrSoftwarePathRenderer.h',
      '<(skia_src_path)/gpu/GrSurfacePriv.h',
      '<(skia_src_path)/gpu/GrSurface.cpp',
      '<(skia_src_path)/gpu/GrSurfaceProxy.cpp',
      '<(skia_src_path)/gpu/GrSwizzle.h',
      '<(skia_src_path)/gpu/GrTexture.cpp',
      '<(skia_src_path)/gpu/GrTextureParamsAdjuster.h',
      '<(skia_src_path)/gpu/GrTextureParamsAdjuster.cpp',
      '<(skia_src_path)/gpu/GrTexturePriv.h',
      '<(skia_src_path)/gpu/GrTextureProvider.cpp',
      '<(skia_src_path)/gpu/GrTextureProxy.cpp',
      '<(skia_src_path)/gpu/GrTextureToYUVPlanes.cpp',
      '<(skia_src_path)/gpu/GrTextureToYUVPlanes.h',
      '<(skia_src_path)/gpu/GrTextureAccess.cpp',
      '<(skia_src_path)/gpu/GrTRecorder.h',
      '<(skia_src_path)/gpu/GrUserStencilSettings.h',
      '<(skia_src_path)/gpu/GrWindowRectangles.h',
      '<(skia_src_path)/gpu/GrWindowRectsState.h',
      '<(skia_src_path)/gpu/GrXferProcessor.cpp',
      '<(skia_src_path)/gpu/GrYUVProvider.cpp',
      '<(skia_src_path)/gpu/GrYUVProvider.h',

      # Batches
      '<(skia_src_path)/gpu/batches/GrAAHairLinePathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrAAHairLinePathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrAALinearizingConvexPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrAALinearizingConvexPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrAAConvexTessellator.cpp',
      '<(skia_src_path)/gpu/batches/GrAAConvexTessellator.h',
      '<(skia_src_path)/gpu/batches/GrAADistanceFieldPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrAADistanceFieldPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrAAConvexPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrAAConvexPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrAAFillRectBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrAAFillRectBatch.h',
      '<(skia_src_path)/gpu/batches/GrAAStrokeRectBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrAAStrokeRectBatch.h',
      '<(skia_src_path)/gpu/batches/GrAnalyticRectBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrAnalyticRectBatch.h',
      '<(skia_src_path)/gpu/batches/GrAtlasTextBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrAtlasTextBatch.h',
      '<(skia_src_path)/gpu/batches/GrBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrBatch.h',
      '<(skia_src_path)/gpu/batches/GrClearBatch.h',
      '<(skia_src_path)/gpu/batches/GrClearStencilClipBatch.h',
      '<(skia_src_path)/gpu/batches/GrCopySurfaceBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrCopySurfaceBatch.h',
      '<(skia_src_path)/gpu/batches/GrDashLinePathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrDashLinePathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrDefaultPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrDefaultPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrDiscardBatch.h',
      '<(skia_src_path)/gpu/batches/GrDrawBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrDrawBatch.h',
      '<(skia_src_path)/gpu/batches/GrDrawAtlasBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrDrawAtlasBatch.h',
      '<(skia_src_path)/gpu/batches/GrDrawPathBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrDrawPathBatch.h',
      '<(skia_src_path)/gpu/batches/GrDrawVerticesBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrDrawVerticesBatch.h',
      '<(skia_src_path)/gpu/batches/GrMSAAPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrMSAAPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrNonAAFillRectBatch.h',
      '<(skia_src_path)/gpu/batches/GrNonAAFillRectBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrNonAAFillRectPerspectiveBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrNonAAStrokeRectBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrNonAAStrokeRectBatch.h',
      '<(skia_src_path)/gpu/batches/GrNinePatch.cpp',
      '<(skia_src_path)/gpu/batches/GrNinePatch.h',
      '<(skia_src_path)/gpu/batches/GrPLSPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrPLSPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrRectBatchFactory.h',
      '<(skia_src_path)/gpu/batches/GrRectBatchFactory.cpp',
      '<(skia_src_path)/gpu/batches/GrRegionBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrRegionBatch.h',
      '<(skia_src_path)/gpu/batches/GrStencilAndCoverPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrStencilAndCoverPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrStencilPathBatch.h',
      '<(skia_src_path)/gpu/batches/GrTessellatingPathRenderer.cpp',
      '<(skia_src_path)/gpu/batches/GrTessellatingPathRenderer.h',
      '<(skia_src_path)/gpu/batches/GrVertexBatch.cpp',
      '<(skia_src_path)/gpu/batches/GrVertexBatch.h',

      '<(skia_src_path)/gpu/effects/Gr1DKernelEffect.h',
      '<(skia_src_path)/gpu/effects/GrConfigConversionEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrConfigConversionEffect.h',
      '<(skia_src_path)/gpu/effects/GrConstColorProcessor.cpp',
      '<(skia_src_path)/gpu/effects/GrCoverageSetOpXP.cpp',
      '<(skia_src_path)/gpu/effects/GrCustomXfermode.cpp',
      '<(skia_src_path)/gpu/effects/GrBezierEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrBezierEffect.h',
      '<(skia_src_path)/gpu/effects/GrConvolutionEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrConvolutionEffect.h',
      '<(skia_src_path)/gpu/effects/GrConvexPolyEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrConvexPolyEffect.h',
      '<(skia_src_path)/gpu/effects/GrBicubicEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrBicubicEffect.h',
      '<(skia_src_path)/gpu/effects/GrBitmapTextGeoProc.cpp',
      '<(skia_src_path)/gpu/effects/GrBitmapTextGeoProc.h',
      '<(skia_src_path)/gpu/effects/GrDashingEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrDashingEffect.h',
      '<(skia_src_path)/gpu/effects/GrDisableColorXP.cpp',
      '<(skia_src_path)/gpu/effects/GrDisableColorXP.h',
      '<(skia_src_path)/gpu/effects/GrDistanceFieldGeoProc.cpp',
      '<(skia_src_path)/gpu/effects/GrDistanceFieldGeoProc.h',
      '<(skia_src_path)/gpu/effects/GrDitherEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrDitherEffect.h',
      '<(skia_src_path)/gpu/effects/GrGammaEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrGammaEffect.h',
      '<(skia_src_path)/gpu/effects/GrMatrixConvolutionEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrMatrixConvolutionEffect.h',
      '<(skia_src_path)/gpu/effects/GrOvalEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrOvalEffect.h',
      '<(skia_src_path)/gpu/effects/GrPorterDuffXferProcessor.cpp',
      '<(skia_src_path)/gpu/effects/GrRRectEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrRRectEffect.h',
      '<(skia_src_path)/gpu/effects/GrSimpleTextureEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrSimpleTextureEffect.h',
      '<(skia_src_path)/gpu/effects/GrSingleTextureEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrSingleTextureEffect.h',
      '<(skia_src_path)/gpu/effects/GrTextureDomain.cpp',
      '<(skia_src_path)/gpu/effects/GrTextureDomain.h',
      '<(skia_src_path)/gpu/effects/GrTextureStripAtlas.cpp',
      '<(skia_src_path)/gpu/effects/GrXfermodeFragmentProcessor.cpp',
      '<(skia_src_path)/gpu/effects/GrYUVEffect.cpp',
      '<(skia_src_path)/gpu/effects/GrYUVEffect.h',

      '<(skia_src_path)/gpu/instanced/InstancedRendering.cpp',
      '<(skia_src_path)/gpu/instanced/InstancedRendering.h',
      '<(skia_src_path)/gpu/instanced/InstancedRenderingTypes.h',
      '<(skia_src_path)/gpu/instanced/InstanceProcessor.cpp',
      '<(skia_src_path)/gpu/instanced/InstanceProcessor.h',
      '<(skia_src_path)/gpu/instanced/GLInstancedRendering.cpp',
      '<(skia_src_path)/gpu/instanced/GLInstancedRendering.h',

      # text
      '<(skia_src_path)/gpu/text/GrAtlasTextBlob.cpp',
      '<(skia_src_path)/gpu/text/GrAtlasTextBlob_regenInBatch.cpp',
      '<(skia_src_path)/gpu/text/GrAtlasTextBlob.h',
      '<(skia_src_path)/gpu/text/GrAtlasTextContext.cpp',
      '<(skia_src_path)/gpu/text/GrAtlasTextContext.h',
      '<(skia_src_path)/gpu/text/GrBatchFontCache.cpp',
      '<(skia_src_path)/gpu/text/GrBatchFontCache.h',
      '<(skia_src_path)/gpu/text/GrDistanceFieldAdjustTable.cpp',
      '<(skia_src_path)/gpu/text/GrDistanceFieldAdjustTable.h',
      '<(skia_src_path)/gpu/text/GrStencilAndCoverTextContext.cpp',
      '<(skia_src_path)/gpu/text/GrStencilAndCoverTextContext.h',
      '<(skia_src_path)/gpu/text/GrTextBlobCache.cpp',
      '<(skia_src_path)/gpu/text/GrTextBlobCache.h',
      '<(skia_src_path)/gpu/text/GrTextUtils.cpp',
      '<(skia_src_path)/gpu/text/GrTextUtils.h',

      '<(skia_src_path)/gpu/gl/GrGLAssembleInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLBuffer.cpp',
      '<(skia_src_path)/gpu/gl/GrGLBuffer.h',
      '<(skia_src_path)/gpu/gl/GrGLCaps.cpp',
      '<(skia_src_path)/gpu/gl/GrGLCaps.h',
      '<(skia_src_path)/gpu/gl/GrGLContext.cpp',
      '<(skia_src_path)/gpu/gl/GrGLContext.h',
      '<(skia_src_path)/gpu/gl/GrGLCreateNativeInterface_none.cpp',
      '<(skia_src_path)/gpu/gl/GrGLCreateNullInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLDefaultInterface_none.cpp',
      '<(skia_src_path)/gpu/gl/GrGLDefines.h',
      '<(skia_src_path)/gpu/gl/GrGLGLSL.cpp',
      '<(skia_src_path)/gpu/gl/GrGLGLSL.h',
      '<(skia_src_path)/gpu/gl/GrGLGpu.cpp',
      '<(skia_src_path)/gpu/gl/GrGLGpu.h',
      '<(skia_src_path)/gpu/gl/GrGLGpuCommandBuffer.h',
      '<(skia_src_path)/gpu/gl/GrGLGpuProgramCache.cpp',
      '<(skia_src_path)/gpu/gl/GrGLExtensions.cpp',
      '<(skia_src_path)/gpu/gl/GrGLInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLIRect.h',
      '<(skia_src_path)/gpu/gl/GrGLPath.cpp',
      '<(skia_src_path)/gpu/gl/GrGLPath.h',
      '<(skia_src_path)/gpu/gl/GrGLPathRange.cpp',
      '<(skia_src_path)/gpu/gl/GrGLPathRange.h',
      '<(skia_src_path)/gpu/gl/GrGLPathRendering.cpp',
      '<(skia_src_path)/gpu/gl/GrGLPathRendering.h',
      '<(skia_src_path)/gpu/gl/GrGLProgram.cpp',
      '<(skia_src_path)/gpu/gl/GrGLProgram.h',
      '<(skia_src_path)/gpu/gl/GrGLProgramDataManager.cpp',
      '<(skia_src_path)/gpu/gl/GrGLProgramDataManager.h',
      '<(skia_src_path)/gpu/gl/GrGLRenderTarget.cpp',
      '<(skia_src_path)/gpu/gl/GrGLRenderTarget.h',
      '<(skia_src_path)/gpu/gl/GrGLSampler.h',
      '<(skia_src_path)/gpu/gl/GrGLStencilAttachment.cpp',
      '<(skia_src_path)/gpu/gl/GrGLStencilAttachment.h',
      '<(skia_src_path)/gpu/gl/GrGLTestInterface.cpp',
      '<(skia_src_path)/gpu/gl/GrGLTestInterface.h',
      '<(skia_src_path)/gpu/gl/GrGLTexture.cpp',
      '<(skia_src_path)/gpu/gl/GrGLTexture.h',
      '<(skia_src_path)/gpu/gl/GrGLTextureRenderTarget.cpp',
      '<(skia_src_path)/gpu/gl/GrGLTextureRenderTarget.h',
      '<(skia_src_path)/gpu/gl/GrGLUtil.cpp',
      '<(skia_src_path)/gpu/gl/GrGLUtil.h',
      '<(skia_src_path)/gpu/gl/GrGLUniformHandler.cpp',
      '<(skia_src_path)/gpu/gl/GrGLUniformHandler.h',
      '<(skia_src_path)/gpu/gl/GrGLVaryingHandler.cpp',
      '<(skia_src_path)/gpu/gl/GrGLVaryingHandler.h',
      '<(skia_src_path)/gpu/gl/GrGLVertexArray.cpp',
      '<(skia_src_path)/gpu/gl/GrGLVertexArray.h',

      # Files for building GLSL shaders
      '<(skia_src_path)/gpu/gl/builders/GrGLProgramBuilder.cpp',
      '<(skia_src_path)/gpu/gl/builders/GrGLProgramBuilder.h',
      '<(skia_src_path)/gpu/gl/builders/GrGLShaderStringBuilder.cpp',
      '<(skia_src_path)/gpu/gl/builders/GrGLShaderStringBuilder.h',
      '<(skia_src_path)/gpu/gl/builders/GrGLSLPrettyPrint.cpp',

      # GLSL
      '<(skia_src_path)/gpu/glsl/GrGLSL.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSL.h',
      '<(skia_src_path)/gpu/glsl/GrGLSL_impl.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLBlend.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLBlend.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLCaps.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLCaps.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLColorSpaceXformHelper.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLFragmentProcessor.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLFragmentProcessor.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLFragmentShaderBuilder.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLFragmentShaderBuilder.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLGeometryProcessor.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLGeometryProcessor.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLGeometryShaderBuilder.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLGeometryShaderBuilder.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLPrimitiveProcessor.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLPrimitiveProcessor.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLProgramBuilder.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLProgramBuilder.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLProgramDataManager.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLProgramDataManager.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLSampler.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLShaderBuilder.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLShaderBuilder.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLShaderVar.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLUniformHandler.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLUtil.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLUtil.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLVarying.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLVarying.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLVertexShaderBuilder.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLVertexShaderBuilder.h',
      '<(skia_src_path)/gpu/glsl/GrGLSLXferProcessor.cpp',
      '<(skia_src_path)/gpu/glsl/GrGLSLXferProcessor.h',

      # Sk files
      '<(skia_include_path)/gpu/SkGr.h',

      '<(skia_src_path)/gpu/SkGpuDevice.cpp',
      '<(skia_src_path)/gpu/SkGpuDevice.h',
      '<(skia_src_path)/gpu/SkGpuDevice_drawTexture.cpp',
      '<(skia_src_path)/gpu/SkGr.cpp',
      '<(skia_src_path)/gpu/SkGrPriv.h',

      '<(skia_src_path)/image/SkImage_Gpu.h',
      '<(skia_src_path)/image/SkImage_Gpu.cpp',
      '<(skia_src_path)/image/SkSurface_Gpu.h',
      '<(skia_src_path)/image/SkSurface_Gpu.cpp',
    ],
    'skgpu_vk_sources': [
      '<(skia_include_path)/gpu/vk/GrVkBackendContext.h',
      '<(skia_include_path)/gpu/vk/GrVkDefines.h',
      '<(skia_include_path)/gpu/vk/GrVkInterface.h',
      '<(skia_include_path)/gpu/vk/GrVkTypes.h',
      '<(skia_src_path)/gpu/vk/GrVkBackendContext.cpp',
      '<(skia_src_path)/gpu/vk/GrVkBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkBuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkCaps.cpp',
      '<(skia_src_path)/gpu/vk/GrVkCaps.h',
      '<(skia_src_path)/gpu/vk/GrVkCommandBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkCommandBuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkCopyManager.cpp',
      '<(skia_src_path)/gpu/vk/GrVkCopyManager.h',
      '<(skia_src_path)/gpu/vk/GrVkCopyPipeline.cpp',
      '<(skia_src_path)/gpu/vk/GrVkCopyPipeline.h',
      '<(skia_src_path)/gpu/vk/GrVkDescriptorPool.cpp',
      '<(skia_src_path)/gpu/vk/GrVkDescriptorPool.h',
      '<(skia_src_path)/gpu/vk/GrVkDescriptorSet.cpp',
      '<(skia_src_path)/gpu/vk/GrVkDescriptorSet.h',
      '<(skia_src_path)/gpu/vk/GrVkDescriptorSetManager.cpp',
      '<(skia_src_path)/gpu/vk/GrVkDescriptorSetManager.h',
      '<(skia_src_path)/gpu/vk/GrVkExtensions.cpp',
      '<(skia_src_path)/gpu/vk/GrVkExtensions.h',
      '<(skia_src_path)/gpu/vk/GrVkFramebuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkFramebuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkGLSLSampler.h',
      '<(skia_src_path)/gpu/vk/GrVkGpu.cpp',
      '<(skia_src_path)/gpu/vk/GrVkGpu.h',
      '<(skia_src_path)/gpu/vk/GrVkGpuCommandBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkGpuCommandBuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkImage.cpp',
      '<(skia_src_path)/gpu/vk/GrVkImage.h',
      '<(skia_src_path)/gpu/vk/GrVkImageView.cpp',
      '<(skia_src_path)/gpu/vk/GrVkImageView.h',
      '<(skia_src_path)/gpu/vk/GrVkIndexBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkIndexBuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkInterface.cpp',
      '<(skia_src_path)/gpu/vk/GrVkMemory.cpp',
      '<(skia_src_path)/gpu/vk/GrVkMemory.h',
      '<(skia_src_path)/gpu/vk/GrVkPipeline.cpp',
      '<(skia_src_path)/gpu/vk/GrVkPipeline.h',
      '<(skia_src_path)/gpu/vk/GrVkPipelineState.cpp',
      '<(skia_src_path)/gpu/vk/GrVkPipelineState.h',
      '<(skia_src_path)/gpu/vk/GrVkPipelineStateBuilder.cpp',
      '<(skia_src_path)/gpu/vk/GrVkPipelineStateBuilder.h',
      '<(skia_src_path)/gpu/vk/GrVkPipelineStateCache.cpp',
      '<(skia_src_path)/gpu/vk/GrVkPipelineStateDataManager.cpp',
      '<(skia_src_path)/gpu/vk/GrVkPipelineStateDataManager.h',
      '<(skia_src_path)/gpu/vk/GrVkRenderPass.cpp',
      '<(skia_src_path)/gpu/vk/GrVkRenderPass.h',
      '<(skia_src_path)/gpu/vk/GrVkRenderTarget.cpp',
      '<(skia_src_path)/gpu/vk/GrVkRenderTarget.h',
      '<(skia_src_path)/gpu/vk/GrVkResource.h',
      '<(skia_src_path)/gpu/vk/GrVkResourceProvider.cpp',
      '<(skia_src_path)/gpu/vk/GrVkResourceProvider.h',
      '<(skia_src_path)/gpu/vk/GrVkSampler.cpp',
      '<(skia_src_path)/gpu/vk/GrVkSampler.h',
      '<(skia_src_path)/gpu/vk/GrVkStencilAttachment.cpp',
      '<(skia_src_path)/gpu/vk/GrVkStencilAttachment.h',
      '<(skia_src_path)/gpu/vk/GrVkTexture.cpp',
      '<(skia_src_path)/gpu/vk/GrVkTexture.h',
      '<(skia_src_path)/gpu/vk/GrVkTextureRenderTarget.cpp',
      '<(skia_src_path)/gpu/vk/GrVkTextureRenderTarget.h',
      '<(skia_src_path)/gpu/vk/GrVkTransferBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkTransferBuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkUniformBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkUniformBuffer.h',
      '<(skia_src_path)/gpu/vk/GrVkUniformHandler.cpp',
      '<(skia_src_path)/gpu/vk/GrVkUniformHandler.h',
      '<(skia_src_path)/gpu/vk/GrVkUtil.cpp',
      '<(skia_src_path)/gpu/vk/GrVkUtil.h',
      '<(skia_src_path)/gpu/vk/GrVkVaryingHandler.cpp',
      '<(skia_src_path)/gpu/vk/GrVkVaryingHandler.h',
      '<(skia_src_path)/gpu/vk/GrVkVertexBuffer.cpp',
      '<(skia_src_path)/gpu/vk/GrVkVertexBuffer.h',
    ],
    'skgpu_native_gl_sources': [
      '<(skia_src_path)/gpu/gl/GrGLDefaultInterface_native.cpp',
      '<(skia_src_path)/gpu/gl/mac/GrGLCreateNativeInterface_mac.cpp',
      '<(skia_src_path)/gpu/gl/win/GrGLCreateNativeInterface_win.cpp',
      '<(skia_src_path)/gpu/gl/glx/GrGLCreateNativeInterface_glx.cpp',
      '<(skia_src_path)/gpu/gl/egl/GrGLCreateNativeInterface_egl.cpp',
      '<(skia_src_path)/gpu/gl/iOS/GrGLCreateNativeInterface_iOS.cpp',
      '<(skia_src_path)/gpu/gl/android/GrGLCreateNativeInterface_android.cpp',
    ],
    'skgpu_null_gl_sources': [
    ],
  },
}